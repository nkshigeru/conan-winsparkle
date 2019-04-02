import os
from conans import ConanFile, tools


class WinsparkleConan(ConanFile):
    name = "winsparkle"
    version = "0.6.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Winsparkle here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "arch"
    no_copy_source = True

    def source(self):
        url = "https://github.com/vslavik/winsparkle/releases/download/v{version}/WinSparkle-{version}.zip".format(version=self.version)
        tools.get(url)
        os.rename("WinSparkle-{version}".format(version=self.version), "WinSparkle")

    def package(self):
        self.copy("*.h", dst="include", src="WinSparkle/include", keep_path=False)
        release_dir = "WinSparkle/Release" if self.settings.arch == "x86" else "WinSparkle/x64/Release/"
        self.copy("*.lib", dst="lib", src=release_dir, keep_path=False)
        self.copy("*.dll", dst="bin", src=release_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["WinSparkle"]
