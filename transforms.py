import torchvision
import io
from PIL import Image
from torchvision import transforms as T
from torchvision.utils import save_image
image=Image.open("./sparrow_picture.jpg")
img=image
print(img)
preprocess = T.Compose([
   T.Resize(256),
   T.CenterCrop(224),
   T.ToTensor(),
   T.Normalize(
       mean=[0.485, 0.456, 0.406],#(value-mean)/std - для каждого из трех rgb каналов (т.е. цвет меняет) делать только после T.ToTensor()
       std=[0.229, 0.224, 0.225]
   )
])

x = preprocess(img)
img_num=0
print(x.shape)
save_image(x, 'img'+str(img_num)+'.png')