# https://github.com/pyinstaller/pyinstaller/issues/3390

import qt5reactor

qt5reactor.install()

print('qt5reactor installed as twisted reactor')
