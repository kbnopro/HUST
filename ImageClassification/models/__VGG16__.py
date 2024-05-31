from torch import nn

class VGG16(nn.Module):
    def __init__(self):
        super(VGG16,self).__init__()

    def forward(self,x):
        return x