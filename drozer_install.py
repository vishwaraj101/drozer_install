import os
print "Installing Dependencies ..."
print "\n"
pwd=os.getcwd()
os.system("wget wget https://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-0.13.tar.gz")
os.system("tar xzvf pyOpenSSL-0.13.tar.gz")
os.chdir("pyOpenSSL-0.13")
os.system("sed -i '' 's/X509_REVOKED_dup/X509_REVOKED_dupe/' OpenSSL/crypto/crl.c")
os.system("python setup.py build_ext -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include")
os.system("python setup.py build")
os.system("python setup.py install")
os.system("sudo easy_install --allow-hosts pypi.python.org protobuf==2.4.1")
os.system("sudo easy_install twisted==10.2.0")
print "\n"
print "Installing drozer...."
os.chdir(pwd)
os.system("sudo easy_install ./drozer-2.3.4-py2.7.egg")
os.system("drozer")
