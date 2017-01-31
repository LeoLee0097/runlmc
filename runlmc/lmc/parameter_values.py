# Copyright (c) 2016, Vladimir Feinberg
# Licensed under the BSD 3-clause license (see LICENSE)

import numpy as np

class ParameterValues:
    def __init__(self, coreg_vecs, coreg_diags, kernels, lens, y, noise):
        self.coreg_vecs = coreg_vecs
        self.coreg_diag = coreg_diags # TODO(cleanup): coreg_diags
        self.kernels = kernels
        self.coreg_mats = [a.T.dot(a) + np.diag(k)
                           for a, k in zip(coreg_vecs, self.coreg_diag)]
        self.lens = lens
        self.noise = noise
        self.y = y
        self.n = len(self.y)
        self.D = len(self.noise)
        self.Q = len(self.coreg_vecs)

    @staticmethod
    def generate(lmc_model):
        return ParameterValues(
            lmc_model.coreg_vecs,
            lmc_model.coreg_diags,
            lmc_model.kernels,
            list(map(len, lmc_model.Xs)),
            lmc_model.y,
            lmc_model.noise)
