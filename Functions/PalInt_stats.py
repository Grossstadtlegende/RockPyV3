# coding=utf-8

'''old from V2'''
# import numpy as np
# import scipy as sp
# from numpy import arctan
#
#
# def DANG():
#     '''
#     The Deviation of the ANGle (DANG; Tauxe and Staudigel, 2004; see Chapter  9):
#     The angle that the direction of the NRM component used in the slope calculations calculated as a best-fit line
#     (see Appendix A.3.5) makes with the angle of the line anchoring the center of mass (see Appendix A.3.5) to the
#     origin (see insert to Fig. C.2a).
#
#     :todo: implement, not urgent since only single component analysis so far
#     '''
#     #todo
#     pass
#
#
# def MAD(x, y, z):
#     """
#     :Parameters:
#        x : array_like
#           x-data
#        y : array_like
#           y-data
#        z : array_like
#           z-data
#
#     :Returns:
#        MAD : float
#
#     Kirschvink [1980] also defined the maximum angle of deviation or (MAD) for each of these. The best-fit line is given by the principal eigenvector V 1 and its MAD is given by:
#
#     .. math::
#
#        \\text{MAD} =  \\tan^{-1} \\left( \\frac{\\sqrt{\\tau_2^2 + \\tau_3^2}}{\\tau_1} \\right)
#
#     """
#     tensor = orientation_tensor(x, y, z)
#     evals = tensor.eigenvalues(norm=True)
#     MAD = arctan(np.sqrt(evals[1] ** 2 + evals[2] ** 2) / evals[0])
#     return MAD
#
#
#
# def scatter(palint_obj, quantity='M', debug=False, **kwargs):
#     #todo chose if not to put in paleointensity class
#     '''
#
#     :Parameters:
#
#        palint_obj : paleointensity object
#           Elements to sum.
#        quantity : string,
#            the magnetic quantity to calculate the scatter parameter for
#        debug : boolean, optional
#            prints information on processed data
#     :Returns:
#        scatter : scatter of points around least squares line
#     :seel also:
#         :py:func:`slope`
#
#
#     The “scatter” parameter :math:`\\beta` : the standard error of the slope σ (assuming uncertainty in both the pTRM and NRM data)
#     over the absolute value of the best-fit slope :math:`|b|` [Coe:1978vg]_.
#
#     '''
#     scatter = palint_obj.slope[quantity][1] / abs(palint_obj.slope[quantity][0])
#
#     return scatter
#
#
# def remanence_f():
#     #todo
#     pass
#
#
# def DRATS():
#     #todo
#     pass
#
#
# def maximum_difference():
#     #todo
#     pass
#
#
# def zig_zag_z():
#     #todo
#     pass
#
#
# def gap_factor():
#     #todo
#     pass
#
#
# def quality_factor():
#     #todo
#     pass
#
#
# def aniso_test():
#     #todo
#     pass
#
#
# def orientation_tensor(x, y, z):
#     '''
#     :Parameters:
#        x : arraylike
#           x-data
#        y : arraylike
#           y-data
#        z : arraylike
#           z-data
#     :Returns:
#
#     Transform the origin of the data cluster to the center of mass:
#
#     .. math::
#
#        x_{1i}' = x_{1i}  - \overline{x_1}
#
#        x_{2i}' = x_{2i}  - \overline{x_2}
#
#        x_{3i}' = x_{3i}  - \overline{x_3}
#
#     where :math:`x_i'` are the transformed coordinates.
#     '''
#
#     from RockPyV2.structure import tensor
#
#     ''' center of mass calculation '''
#     mean_x = np.mean(x, dtype=float)
#     mean_y = np.mean(y, dtype=float)
#     mean_z = np.mean(z, dtype=float)
#
#     ''' center of mass transformation '''
#     diff_x = x - mean_x
#     diff_y = y - mean_y
#     diff_z = z - mean_z
#
#     orientation_matrix = np.array([[np.sum(diff_x * diff_x), np.sum(diff_x * diff_y), np.sum(diff_x * diff_z)],
#                                    [np.sum(diff_y * diff_x), np.sum(diff_y * diff_y), np.sum(diff_y * diff_z)],
#                                    [np.sum(diff_z * diff_x), np.sum(diff_z * diff_y), np.sum(diff_z * diff_z)]])
#     tensor = tensor(orientation_matrix)
#     return tensor
#
#
# if __name__ == '__main__':
#     from RockPyV2 import testdata
#     from RockPyV2 import structure
#
#     data_dict = testdata.PalInt()
#     test_palint_obj = structure.paleointensity(sample_name='3a', sample_mass=324E-3, data=data_dict, treatment=0)
#     # slope(test_palint_obj, debug=True)
#     # scatter(test_palint_obj, debug=True)
#     xyz = test_palint_obj._getvalue('TH')
#     x = xyz['X']
#     y = xyz['Y']
#     z = xyz['Z']
#     print orientation_tensor(x, y, z).eigenvalues(norm=True)
#
# '''
# [Coe:1978vg] Coe, R. S., Grommé, S., & Mankinen, E. A. (1978). Geomagnetic paleointensities from radiocarbon-dated lava flows on Hawaii and the question of the Pacific nondipole low. Journal of Geophysical Research, 83, 1740-1756.
#
# '''