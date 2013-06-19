    def plot_xy(self, figure, idAdj=None, idFix=None, plotTest=False):
        """
        plots figure with points and error ellipses and displacements

        figure: FigureLayoutBase instance or descendant
        idAdj: list of ids of adjusted points to be drawn
               for no adjusted points set idAdj = []
        idFix: plot fixed points
               for no fixed points set idFix = []
        """

        # id of points
        if idAdj is None:
            idAdj = [id for id in self.epochPointList.iter_id()]

        if idFix is None:
            idFix = [id for id in self.pointListAdj.iter_id()]

        # plot adjusted
        if len(idAdj) > 0:
           self.plot_adj(figure, idAdj, plotErrorZ=False, plotTest=plotTest)

        # plot fixed
        if len(idFix) > 0:
            self.plot_fix(figure, idFix)

    def plot_xyz(self, figure, idAdj=None, plotTest=False):
        """
        plots figure with points, error ellipses, displacements
        and confidence interval of z along y axis

        figure: FigureLayoutBase instance or descendant
        idAdj: list of ids of adjusted points to be drawn
               for no adjusted points set idAdj = []
        #idFix: plot fixed points
        #       for no fixed points set idFix = []

        """

        # id of points
        if idAdj is None:
            idAdj = [id for id in self.epochPointList.iter_id()]

        #if idFix is None:
        #    idFix = [id for id in self.pointListFix.iter_id()]

        # plot adjusted
        if len(idAdj) > 0:
           self.plot_adj(figure, idAdj, plotErrorZ=True, plotTest=plotTest)

        # plot fixed
        #if len(idFix) > 0:
        #    self.plot_fix(figure, idFix)


    def plot_z(self, figure, id, plotTest=False):
        """plot x coordinates of point id for all epochs with stdev

        self: EpochList isntance
        id: id or ids of point
        """

        if type(id) is not tuple and type(id) is not list:
            id = (id,)

        # set figure
        figure.set_color_style(self)
        figure.gca().xaxis_date()


        # plot points
        for idi in id:
            self._plot_epoch_list_displacement_z(figure, idi, plotTest)
            figure.reset_epoch_counter()

        # set free space around draw
        figure.set_free_space()

        #update
        figure.update_(self)


    def _plot_epoch_list_displacement_z(self, figure, id, plotTest):
        """
        plot 2D graph of point z coordinates,
        confidence intervals of z coordinates and displacements for all epochs

        id: point id
        plotTest: plot results of test?
        """

        # point iterator
        pointIter = self.epochPointList.iter_point(id)
        # plot points and stdev
        z = [] # z coordinates of points
        for point, date in zip(pointIter, self.dateTimeList):
            point.plot_z(figure, date)
            if plotTest:
                if point.testPassed is not None: # point is tested
                    point.plot_z_stdev(figure, date)
            else:
                point.plot_z_stdev(figure, date)

            figure.next_point_dot_style()
            z.append(point.z)

        point0 = None
        for i, p in enumerate(self.epochPointList.iter_point(id)):
            if p.is_set_z():
                point0 = p
                i_epoch = i
                break

        # label point0
        if point0 is not None:
            point0.x = self.dateTimeList[i_epoch]
            point0.y = point.z
            point0.plot_label(figure)

        # plot vector
        figure.plot_vector_z(self.dateTimeList, z)

        # plot zero line
        if point0 is not None:
            z0 = [point0.z for t in self.dateTimeList]
            figure.plot_vector_z0(self.dateTimeList, z0)


    def plot_fix(self, figure, id):
        """
        plots 2D graph of fixed points
        """

        figure.set_aspect_equal()
        figure.update_(self)

        for idi in id:
            self.pointListAdj.plot_(figure)

        # set free space around draw
        figure.set_free_space()


    def plot_adj(self, figure, id, plotErrorZ, plotTest):
        """
        plots 2D graph of adjusted points, displacements and error ellipses

        figure: FigureLayoutBase instance
        id: id or ids of point
        plotErrorZ: plot confidence interval of z coordinate?
        plotTest: plot results of test?
        """

        if type(id) is not tuple and type(id) is not list:
            id = [id]

        # update figure
        figure.set_aspect_equal()
        figure.update_(self)

        # plot points
        for idi in id:
            self._plot_epoch_list_displacement_xy(figure, idi, plotErrorZ,
                                                plotTest)
            figure.reset_epoch_counter()

        # set free space around draw
        figure.set_free_space()

    def _plot_epoch_list_displacement_xy(self, figure, id,
                                          plotErrorZ, plotTest):
        """
        plot 2D graph of point ,
        error ellipses and displacements for all epochs
        and optionally confidence interval of z coordinate along y axis

        id: point id
        plotErrorZ: plot confidence interval of z coordinate?
        plotTest: plot results of test?
        """

        # find zero epoch for point
        # the first point with x!=None and y!=None
        point0 = None
        for p in self.epochPointList.iter_point(id, withNone=False):
            if p.x != None and p.y != None:
                point0 = p
                #x0, y0 = point0.x, point0.y
                break
        if point0 == None:
            return # no xy point available

        # save coordinates of vector with scale
        pointScaled = [] # point list as normal list
        for p in self.epochPointList.iter_point(id, withNone=True):
            if plotTest and isinstance(p, PointLocalGamaDisplTest):
                    covmat = p.displ.get_point_cov_mat()
            else:
                covmat = p.get_point_cov_mat()
            ps = (p - point0)*figure.errScale + point0
            ps.covmat = covmat
            #import sys
            #print >>sys.stderr, "Point: %s" % ps.id
            #print >>sys.stderr, "epl: %s" % type(ps)
            pointScaled.append(ps)

        # plot points and error ellipses
        for p in pointScaled:
            p.plot_(figure, plotLabel=False)
            figure.set_stdev(self) # sets StandardDeviation instance for epoch
            if plotTest and isinstance(p, PointLocalGamaDisplTest):
                if p.testPassed is not None: # point is tested
                    p.plot_error_ellipse(figure)
            else:
                p.plot_error_ellipse(figure)

            figure.next_point_dot_style()

        # label point0
        point0_label = copy.deepcopy(point0)
        point0_label.id = id
        point0_label.plot_label(figure)

        # plot vector
        figure.plot_vector_xy(pointScaled)


