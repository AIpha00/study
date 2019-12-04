# CMake generated Testfile for 
# Source directory: /Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video
# Build directory: /Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/modules/video
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_video "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/bin/opencv_test_video" "--gtest_output=xml:opencv_test_video.xml")
set_tests_properties(opencv_test_video PROPERTIES  LABELS "Main;opencv_video;Accuracy" WORKING_DIRECTORY "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/test-reports/accuracy" _BACKTRACE_TRIPLES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVUtils.cmake;1154;add_test;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;1168;ocv_add_test_from_target;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;979;ocv_add_accuracy_tests;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;2;ocv_define_module;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;0;")
add_test(opencv_perf_video "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/bin/opencv_perf_video" "--gtest_output=xml:opencv_perf_video.xml")
set_tests_properties(opencv_perf_video PROPERTIES  LABELS "Main;opencv_video;Performance" WORKING_DIRECTORY "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/test-reports/performance" _BACKTRACE_TRIPLES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVUtils.cmake;1154;add_test;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;1090;ocv_add_test_from_target;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;980;ocv_add_perf_tests;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;2;ocv_define_module;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;0;")
add_test(opencv_sanity_video "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/bin/opencv_perf_video" "--gtest_output=xml:opencv_perf_video.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_video PROPERTIES  LABELS "Main;opencv_video;Sanity" WORKING_DIRECTORY "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/release/test-reports/sanity" _BACKTRACE_TRIPLES "/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVUtils.cmake;1154;add_test;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;1091;ocv_add_test_from_target;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/cmake/OpenCVModule.cmake;980;ocv_add_perf_tests;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;2;ocv_define_module;/Users/lvsongke/coding/lvsk/OCR/opencv-3.4.0/modules/video/CMakeLists.txt;0;")
