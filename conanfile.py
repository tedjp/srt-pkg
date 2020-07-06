from conans import ConanFile, CMake, tools

class SrtConan(ConanFile):
    name = "srt"
    version = "1.4.1"
    license = "MPLv2.0"
    author = "Ted Percival <ted@tedp.id.au>"
    url = "https://github.com/tedjp/srt-pkg"
    description = "Secure Reliable Transport"
    topics = ("protocol", "secure", "reliable", "transport")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    requires = ["openssl/1.1.1g"]
    generators = [
        "cmake",
        "cmake_find_package",
        "cmake_paths",
    ]

    scm = {
        "type": "git",
        "subfolder": "srt",
        "url": "https://github.com/Haivision/srt.git",
        "revision": "v1.4.1"
    }

    def source(self):
        # Nothing to do :-)
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure(args=['-DCMAKE_TOOLCHAIN_FILE=conan_paths.cmake'], source_folder="srt")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*srt.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so.*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["srt"]
