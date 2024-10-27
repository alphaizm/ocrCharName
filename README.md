# ocrCharName
### python venv
```
python -m venv .venv
```

## Ready EasyOCR

### PyTorch

https://pytorch.org/

PyTorch Build：Stable (2.3.1)  
Your OS：Windows  
Package：Pip  
Language：Python  
Compute Platform：CPU  
---
Run this Command：  
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### EasyOCR

https://www.jaided.ai/easyocr/install/

$ pip install easyocr

## Ready PaddleOCR ※結局、PaddleOCRを動かせなかった
https://github.com/PaddlePaddle/PaddleOCR

### 2024/07 頃でのトライ
#### PaddleOCR
install the CPU version  
$ python -m pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple

install the GPU version  
$ pip install paddlepaddle-gpu -i https://pypi.tuna.tsinghua.edu.cn/simple

$ python -m pip install paddlepaddle-gpu==2.6.1.post120 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html

Install PaddleOCR Whl Package  
$ pip install "paddleocr>=2.7.3"  
 _※python-3.12　ではインストールエラーになる_


CUDA

CUDA Toolkit Archive  
https://developer.nvidia.com/cuda-toolkit-archive

cuDNN Archive  
https://developer.nvidia.com/rdp/cudnn-archive#a-collapse881-120

C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vXX.XX
以下をコピー
- bin
- include
- lib

パスを通す  
Issue the control sysdm.cpl command.  
タブ：詳細設定を選択  
ボタン：環境変数(N)...  
Path：C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\bin  

## 2024/10 頃でのトライ
#### PaddleOCR
install the CPU version 
```terminal
NG python -m pip install paddlepaddle-gpu==3.0.0b1 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/
OK python -m pip install paddlepaddle-gpu==2.6.1.post120 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
OK python -m pip install paddlepaddle-gpu==2.6.2 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html
```
↓
```
python -m pip install paddleocr
```


## Crop Image
### Image

$ pip install Image

# ADB (BlueStacks)
"C:\Program Files\BlueStacks_nxt\HD-Adb.exe"

$ .\HD-Adb.exe devices  
> List of devices attached
> * daemon not running. starting it now on port 5037 *
> * daemon started successfully *
> emulator-5554   device

$ .\HD-Adb.exe connect 127.0.0.1:5555
> connected to 127.0.0.1:5555

$ .\HD-Adb.exe -s 127.0.0.1:5555 shell pm list package
> package:com.android.internal.display.cutout.emulation.corner
> package:com.android.internal.display.cutout.emulation.double
> package:com.location.provider
> package:com.android.providers.telephony
> package:com.android.providers.calendar
> package:com.android.providers.media
> package:com.google.android.onetimeinitializer
> package:com.google.android.ext.shared
> package:com.android.documentsui
> package:com.android.externalstorage
> package:com.android.htmlviewer
> package:com.android.companiondevicemanager
> package:com.android.providers.downloads
> package:com.android.defcontainer
> package:com.android.providers.downloads.ui
> package:com.android.vending
> package:com.android.pacprocessor
> package:com.android.simappdialog
> package:com.android.internal.display.cutout.emulation.tall
> package:com.android.certinstaller
> package:com.android.carrierconfig
> package:android
> package:com.android.contacts
> package:com.android.camera2
> package:com.android.provision
> package:com.android.statementservice
> package:com.android.settings.intelligence
> package:com.android.systemui.theme.dark
> package:com.android.providers.settings
> package:com.android.printspooler
> package:com.android.inputdevices
> package:com.gof.global
> package:com.google.android.apps.nbu.files
> package:com.google.android.syncadapters.contacts
> package:com.android.keychain
> package:com.android.chrome
> package:com.android.gallery3d
> package:com.google.android.gms
> package:com.google.android.gsf
> package:android.ext.services
> package:com.google.android.partnersetup
> package:com.android.packageinstaller
> package:com.android.carrierdefaultapp
> package:com.android.proxyhandler
> package:com.android.inputmethod.latin
> package:com.google.android.syncadapters.calendar
> package:gg.now.billing.interceptor
> package:gg.now.billing.service
> package:com.google.android.gsf.login
> package:com.android.wallpaper.livepicker
> package:com.google.android.backuptransport
> package:com.android.storagemanager
> package:com.android.bookmarkprovider
> package:com.android.settings
> package:gg.now.billing.service2
> package:com.android.vpndialogs
> package:com.android.phone
> package:com.android.shell
> package:com.android.providers.userdictionary
> package:com.android.location.fused
> package:com.android.systemui
> package:com.uncube.launcher3
> package:com.android.traceur
> package:com.google.android.gms.setup
> package:com.google.android.play.games
> package:com.uncube.gamevantage
> package:gg.now.accounts
> package:com.android.wallpaperpicker
> package:com.android.providers.contacts
> package:com.android.captiveportallogin
