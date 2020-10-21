import matplotlib.pyplot as plt

class SliceViewer:

    def __init__(self, subject):

        self.subject = subject
        self.vertex  = self.subject.shape[0]

    def triple_view(self, i=None):

        if i is None:
            i = self.vertex

        saggital = self.subject[i, :, :]
        axial    = self.subject[:, i, :]
        coronal  = self.subject[:, :, i]

        fig, axes = plt.subplots(1, 3)
        for i, s in enumerate([saggital, axial, coronal]):
            axes[i].imshow(s.T, cmap="gray", origin="lower")


    def single_view(self, view='axial', i):

        pass

    def ratio_view(self, view='axial', threshold=.85):

        for i in range(0, self.vertex):
            
            if view == 'saggital' : slce = sample[:, i, :]
            elif view == 'axial'  : slce = sample[:, i, :]
            elif view == 'coronal': slce = sample[:, i, :]
            else: pass