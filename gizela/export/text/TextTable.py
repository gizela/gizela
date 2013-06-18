# gizela
#
# Copyright (C) 2010 Michal Seidl, Tomas Kubin
# Author: Tomas Kubin <tomas.kubin@fsv.cvut.cz>
# URL: <http://geo.fsv.cvut.cz/gwiki/gizela>

from gizela.util.Error import Error
import sys
import math


class TextTableError(Error):
    pass


class TextTable(object):
    '''
    Makes formatted text table

    classes: PointList
             PointListCovMat
             PointListEpoch
    '''

    def __init__(self, instance, type="border"):
        '''
        @type instance: PointList, PointListCovMat, PointListEpoch
        @param instance: instance to be printed

        @type type: C{str}
        @param type: type of border - border, plain, noborder
        '''

        self._instance = instance

    def __str__(self):
        return "TextTable for instance: '{}'\n".format(self._instance.__class__)

    def __iterData_PointList_default(self):
        '''
        generator for data of type PointList
        '''
        from gizela.adj.local.POINT_LOCAL_STATUS import xmlAttribute
        for point in self._instance:
            yield point.id
            yield point.x
            yield point.y
            yield point.z
            yield xmlAttribute(point)

    def __labelFormat_PointList_default(self):
        '''
        returns tuple of tuples with labels and formats of columns

        ('label', ... label of column
         '{}'   , ... format for data
         'right') ... column alignment
        '''
        return tuple([('id', '{}', 'left'),
                     ('x', '{:.3f}', 'right'),
                     ('y', '{:.3f}', 'right'),
                     ('z', '{:.3f}', 'right'),
                     ('status', '{}', 'left')])

    def __iterData_PointListCovMat_default(self):
        '''
        generator for data of type PointList
        '''
        from gizela.adj.local.POINT_LOCAL_STATUS import xmlAttribute
        for point in self._instance:
            cmList = point.getPointCovMatListWithNones()
            stdev = []
            for val in cmList:
                if val is not None:
                    stdev.append(math.sqrt(val))
                else:
                    stdev.append(val)
            yield point.id
            yield point.x
            yield point.y
            yield point.z
            yield stdev[0]
            yield stdev[2]
            yield stdev[5]
            yield xmlAttribute(point)

    def __labelFormat_PointListCovMat_default(self):
        '''
        returns tuple of tuples with labels and formats of columns

        ('label', ... label of column
         '{}'   , ... format for data
         'right') ... column alignment
        '''
        return tuple([('id', '{}', 'left'),
                     ('x', '{:.3f}', 'right'),
                     ('y', '{:.3f}', 'right'),
                     ('z', '{:.3f}', 'right'),
                     ('sigma_x', '{:.4f}', 'right'),
                     ('sigma_y', '{:.4f}', 'right'),
                     ('sigma_z', '{:.4f}', 'right'),
                     ('status', '{}', 'left')])

    def write(self, file=sys.stdout, border='border', style='default'):
        '''
        generates output text

        @type file: L{FILE} object
        @param file: file object for output

        @type style: C{STR}
        @param style: name of style
        '''
        module = self._instance.__module__
        cls = module.split('.')[-1]
        try:
            labelFormat = getattr(self, '_TextTable__labelFormat_' + cls + '_' + style)()
        except Exception:
            raise TextTableError("__labelFormat method for type '{}' is not defined".format(cls))
        try:
            dataIterator = getattr(self, '_TextTable__iterData_' + cls + '_' + style)()
        except Exception:
            raise TextTableError("__iterData method for type '{}' is not defined".format(cls))

        # borders
        if border == "border":
            '''+------+------+
               | lab1 | lab2 |
               +------+------+
               | val1 | val2 |
               | val1 | val2 |
               +------+------+
            '''
            self.corner_left = "+-"
            self.corner_right = "-+"
            self.corner_middle = "-+-"
            self.border_left = "| "
            self.border_right = " |"
            self.border_middle = " | "
            self.line_top = "-"
            self.line_second = "-"
            self.line_bottom = "-"
        elif border == "plain":
            ''' lab1 | lab2
               ------+------
                val1 | val2
                val1 | val2
            '''
            self.corner_left = "-"
            self.corner_right = "-"
            self.corner_middle = "-+-"
            self.border_left = " "
            self.border_right = " "
            self.border_middle = " | "
            self.line_top = None
            self.line_second = "-"
            self.line_bottom = None
        elif border == "noborder":
            ''' lab1   lab2
               -------------
                val1   val2
                val1   val2
            '''
            self.corner_left = " "
            self.corner_right = " "
            #self.corner_middle = "-+-"
            self.corner_middle = "--"
            self.border_left = " "
            self.border_right = " "
            self.border_middle = "  "
            self.line_top = None
            self.line_second = "-"
            self.line_bottom = None
        else:
            raise TextTableError("Unknown type of text table ({})".format(type))

        # read all data through iterator with format
        row = 0  # index of table row
        lenRow = len(labelFormat)
        outputData = []  # list of lists of values in table by rows
        outputData.append([])
        # find maximal width of text
        columnWidth = [len(label) for label, format, alignment in labelFormat]
        for value in dataIterator:
            #print(labelFormat[row][1], value)
            if value is None:
                outputData[-1].append('')
            else:
                outputData[-1].append(labelFormat[row][1].format(value))
            if len(outputData[-1][-1]) > columnWidth[row]:
                columnWidth[row] = len(outputData[-1][-1])
            row += 1
            if row == lenRow:
                row = 0
                outputData.append([])
        outputData.pop()

        outputString = []  # output list of rows

        # make header - 1st line
        if self.line_top is not None:
            outputString.append(self.corner_left +
                                self.corner_middle.join([self.line_top * w for w in columnWidth]) +
                                self.corner_right)
        # 2nd line - header
        outputString.append(self.border_left +
                            self.border_middle.join(
                                ['{{:^{}}}'.format(width).format(label[0]) for width, label in zip(columnWidth, labelFormat)]) +
                            self.border_right)
        # 3rd line - header
        if self.line_second is not None:
            outputString.append(self.corner_left +
                                self.corner_middle.join([self.line_second * width for width in columnWidth]) +
                                self.corner_right)

        # rows of table
        for row in outputData:
            rowStr = self.border_left
            data = []
            for width, value, labform in zip(columnWidth, row, labelFormat):
                if labform[2] == 'right':
                    data.append('{{:>{}}}'.format(width).format(value))
                else:
                    data.append('{{:<{}}}'.format(width).format(value))
            rowStr += self.border_middle.join(data)
            rowStr += self.border_right
            outputString.append(rowStr)

        # bottom line
        if self.line_bottom is not None:
            outputString.append(self.corner_left +
                                self.corner_middle.join([self.line_bottom * w for w in columnWidth]) +
                                self.corner_right)

        outputString.append('')
        file.write('\n'.join(outputString))


if __name__ == "__main__":

    # PointList instance
    from gizela.adj.local.PointLocal import PointLocal
    from gizela.adj.local.PointList import PointList
    from gizela.adj.local.POINT_LOCAL_STATUS import POINT_LOCAL_STATUS

    pl = PointList()
    pl.addPoint(PointLocal(id="A", x=1, y=100, z=10000, status=POINT_LOCAL_STATUS.con_xy))
    pl.addPoint(PointLocal(id="AA", x=10000, y=1, z=1, status=POINT_LOCAL_STATUS.fix))
    pl.addPoint(PointLocal(id="AAAA", z=1, status=POINT_LOCAL_STATUS.fix))
    pl.addPoint(PointLocal(id="AAAAAAAAAA", x=1, y=10000, status=POINT_LOCAL_STATUS.adj))
    print(pl)
    tt = TextTable(pl)
    tt.write(border="border")
    tt.write(border="plain")
    tt.write(border="noborder")

    # PointListCovMat instance
    from gizela.adj.local.PointLocalCovMat import PointLocalCovMat
    from gizela.adj.local.PointListCovMat import PointListCovMat
    import numpy
    c1 = PointLocalCovMat("C1", x=10, y=20, z=30, status=POINT_LOCAL_STATUS.adj)
    c2 = PointLocalCovMat("C2", x=100, y=200, status=POINT_LOCAL_STATUS.adj)
    c3 = PointLocalCovMat("C3", z=3000, status=POINT_LOCAL_STATUS.adj)
    pl = PointListCovMat()
    pl.addPoint(c1)
    pl.addPoint(c2)
    pl.addPoint(c3)
    cm = numpy.array([[1, 0.1, 0.1, 0.1, 0.1, 0.1],
                      [0, 2,   0.2, 0.2, 0.2, 0.2],
                      [0, 0,   3,   0.3, 0.3, 0.3],
                      [0, 0,   0,   4,   0.4, 0.4],
                      [0, 0,   0,   0,   5,   0.5],
                      [0, 0,   0,   0,   0,   6]])
    pl.setCovMat(cm)
    print(pl)
    tt = TextTable(pl)
    tt.write(border="border")
    tt.write(border="plain")
    tt.write(border="noborder")
