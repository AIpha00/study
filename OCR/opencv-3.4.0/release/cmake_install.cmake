# Install script for directory: /Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2" TYPE FILE FILES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/cvconfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencv2" TYPE FILE FILES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/opencv2/opencv_modules.hpp")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/unix-install/opencv.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/OpenCV/OpenCVModules.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/OpenCV/OpenCVModules.cmake"
         "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/CMakeFiles/Export/share/OpenCV/OpenCVModules.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/OpenCV/OpenCVModules-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/OpenCV/OpenCVModules.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/OpenCV" TYPE FILE FILES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/CMakeFiles/Export/share/OpenCV/OpenCVModules.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/OpenCV" TYPE FILE FILES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/CMakeFiles/Export/share/OpenCV/OpenCVModules-release.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/OpenCV" TYPE FILE FILES
    "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/unix-install/OpenCVConfig-version.cmake"
    "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/unix-install/OpenCVConfig.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/OpenCV" TYPE FILE FILES
    "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/platforms/scripts/valgrind.supp"
    "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/platforms/scripts/valgrind_3rdparty.supp"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/zlib/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/libjpeg/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/libtiff/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/libjasper/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/libpng/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/openexr/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/ippiw/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/3rdparty/ittnotify/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/include/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/modules/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/doc/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/data/cmake_install.cmake")
  include("/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/apps/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
