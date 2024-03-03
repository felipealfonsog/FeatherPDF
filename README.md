## FeatherPDF - Lightweight PDF Viewer
#### Description

FeatherPDF is an ultra-lightweight PDF viewer designed for Linux and macOS. It provides a simple and intuitive user interface for reading PDF documents. The project aims to offer a fast and minimalistic PDF reading experience while using minimal system resources.


<img src="./images/fpdf-iconlogo.png" alt="FeatherPDF Logo" width="75" height="75">


![Version](https://img.shields.io/github/release/felipealfonsog/FeatherPDF.svg?style=flat&color=blue)
![Main Language](https://img.shields.io/github/languages/top/felipealfonsog/FeatherPDF.svg?style=flat&color=blue)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)


[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<!--
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
-->

[![Vim](https://img.shields.io/badge/--019733?logo=vim)](https://www.vim.org/)
[![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/)


[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15.9-blue.svg)](https://pypi.org/project/PyQt5/)

#

#### Prerequisites:

Before you begin, ensure you have met the following requirements:

- **Python 3.11:** FeatherPDF requires Python 3.11 or later. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/release/python-311/).

- **PyQt5:** FeatherPDF uses the PyQt5 library for its user interface. You can install PyQt5 using a package manager. For example, on macOS and Linux, you can use Homebrew:


  ```
  brew install python
  ```
  
  ```
  brew install pyqt@5
  ```


#### Screenshots

[![View Screenshots](https://img.shields.io/badge/View-Screenshots-blue)](#)

![Screenshot of the application interface](images/sshot-fpdf-1.0.0.png)

<!-- 
![Screenshot of the application interface](images/linux/sshot-termpdf-4.jpg)
--> 
<!-- 
**Arch Linux** 

![Screenshot of the application interface](images/linux/sshot-termpdf-1.jpg)

**macOS** 

![Screenshot of the application interface](images/mac/sshot-termpdf-1.png)
-->


#### Futures

[![Features](https://img.shields.io/badge/Features-Check%20Them%20Out-green)](#)

- Open and view PDF files with ease.
- Navigate through pages using on-screen controls or mouse scroll.
- Zoom in and out for comfortable reading.
- Return to the first page or navigate to the next/previous pages.
- Responsive and intuitive user interface.
- MIT Licensed - Free and open-source.

#### Version 1.0.0

The current version, 1.0.0, introduces the core functionality of FeatherPDF. Users can open PDF files, navigate through pages, zoom in/out, and enjoy a seamless reading experience.

#### Installation
#### Via AUR using YAY

[![AUR](https://img.shields.io/aur/version/feather-pdf)](https://aur.archlinux.org/packages/feather-pdf)

<!-- 
[![AUR](https://img.shields.io/aur/version/feather-pdf.svg)](https://aur.archlinux.org/packages/feather-pdf)
-->

https://aur.archlinux.org/packages/feather-pdf

FeatherPDF is available on AUR (Arch User Repository), and it can be installed using the `yay` package manager. Follow the steps below to install FeatherPDF:

1. Make sure you have `yay` installed. If not, you can install it with the following command:
   
   ```
   sudo pacman -S yay
   ```
   Once yay is installed, you can install by running the following command:
   
   ```
   yay -S feather-pdf
   ```
This command will automatically fetch the package from AUR and handle the installation process for you.


#### 🤝 Support and Contributions

If you find this project helpful and would like to support its development, there are several ways you can contribute:

- **Code Contributions**: If you're a developer, you can contribute by submitting pull requests with bug fixes, new features, or improvements. Feel free to fork the project and create your own branch to work on.
- **Bug Reports and Feedback**: If you encounter any issues or have suggestions for improvement, please open an issue on the project's GitHub repository. Your feedback is valuable in making the project better.
- **Documentation**: Improving the documentation is always appreciated. If you find any gaps or have suggestions to enhance the project's documentation, please let me know.

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%E2%98%95-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/felipealfonsog)
[![PayPal](https://img.shields.io/badge/Donate%20with-PayPal-00457C?style=flat-square&logo=paypal&logoColor=white)](https://www.paypal.me/felipealfonsog)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-%23EA4AAA?style=flat-square&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/felipealfonsog)

Your support and contributions are greatly appreciated! Thank you for your help in making this project better.


#### 📝Important

[![Experimental Project](https://img.shields.io/badge/Project-Type%3A%20Experimental-blueviolet)](#)

This is an experimental project aimed at bringing a PDF viewer or reader to the terminal environment. The Terminal PDF Viewer leverages the capabilities of the MuPDF library to enable users to view PDF documents directly within the terminal.

This project is still in its experimental (v.0.0.2 - not yet as a 1.0.0 version) stage and may have limitations in terms of features and compatibility. Use at your own discretion.

#### NOTES

To generate the binary: 

```
pyinstaller --onefile featherpdf.py
```

#### 📄 License

This project is licensed under the [MIT License](LICENSE).
