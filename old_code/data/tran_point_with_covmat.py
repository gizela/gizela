    def tran_(self, tran):
        """
        transforms point with its covariance matrix

        tran: Tran2D or Tran3D instance

        Tran2D transforms points xyz and xy. Covariances xz and yz of xyz point
        are left unchanged with this transform. Is this Correct?
        Tran3D transforms only points xyz.
        """

        if isinstance(tran, Tran2D):
            if self.is_set_xyz():
                # transform xyz point with 2D transformation
                self.x, self.y = tran.transform_xy(self.x, self.y)
                cm3 = self.get_point_cov_mat(dim=3)
                cm2 = self.get_point_cov_mat(dim=2)
                cm2.transform_(tran)
                cm3.set_var(0, cm2.get_var(0))
                cm3.set_var(1, cm2.get_var(1))
                cm3.set_cov(0, 1, cm2.get_cov(0, 1))
                self.set_point_cov_mat(cm3)
            elif self.is_set_xy():
                self.x, self.y = tran.transform_xy(self.x, self.y)
                cm = self.get_point_cov_mat(dim=2)
                cm.transform_(tran)
                self.set_point_cov_mat(cm)
            else:
                import sys
                print >>sys.stderr, "point id=%s not transformed" % self.id

        elif isinstance(tran, Tran3D):
            if self.is_set_xyz():
                self.x, self.y, self.z = \
                        tran.transform_xyz(self.x, self.y, self.z)
                cm = self.get_point_cov_mat(dim=3)
                cm.transform_(tran)
                self.set_point_cov_mat(cm)
            else:
                import sys
                print >>sys.stderr, "point id=%s not transformed" % self.id

        else:
            raise PointListError, "Tran2D or Tran3D instance expected"
