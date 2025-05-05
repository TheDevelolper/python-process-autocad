

apt update
apt install -y python3-pip

# download and install the ODA File Converter
wget -O ODAFileConverter.deb https://www.opendesign.com/guestfiles/get?filename=ODAFileConverter_QT6_lnxX64_8.3dll_25.12.deb

sudo dpkg -i ODAFileConverter.deb

rm -rf ODAFileConverter.deb

# install libs needed for ODAFileConverter
sudo apt-get install libgl1-mesa-glx libxkbcommon0 libfontconfig1 -y

# install Qt + Deps
sudo apt install libqt5gui5 libqt5core5a libqt5widgets5 qt5-qmake qtbase5-dev qtwayland5 -y

# tell Qt to use xcb instead of wayland
export QT_QPA_PLATFORM=xcb

# fix broken dependencies
sudo apt-get install -f

cd /usr/lib/x86_64-linux-gnu
sudo ln -s libxcb-util.so.1 libxcb-util.so.0 
cd -

# install pip packages
pip install -r requirements.txt

# adds python path for pytest
export PYTHONPATH="$PYTHONPATH:/workspaces/python-process-autocad/src"

# install comittizen for changelog generation
pip install commitizen
echo "alias cz='python -m commitizen'" >> ~/.bashrc

# lazygit
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
rm lazygit.tar.gz
rm lazygit