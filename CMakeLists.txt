cmake_minimum_required(VERSION 2.6.0)

SET(CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR}/build)

# pull in the pods macros. See cmake/pods.cmake for documentation
set(PROJECT_NAME ppar)
#include(cmake/pods.cmake) -- moving away from the pods build system

# automatically build LCM types. This also defines a number of CMake
# variables, see cmake/lcmtypes.cmake for details
include(cmake/dependencies.cmake)
include(cmake/lcm-general.cmake)

check_for_python()

# this may be duplicating cmake functions
set(_lcmtypes_python_dir ${PROJECT_SOURCE_DIR}/build/include/lcmtypes/)
execute_process(COMMAND mkdir -p ${_lcmtypes_python_dir})

#set(${TARGET_DIR} )

# call lcm-gen and install to _lcm_python_dir defined above..
gen_python_lcmtypes()

#INSTALL(TARGETS ExecutableTarget RUNTIME DESTINATION FOLDER_LOCATION)
install(TARGETS ${PROJECT_SOURCE_DIR}/src/send-message.py RUNTIME DESTINATION bin)


message("Testing")
message(${CMAKE_INSTALL_PREFIX})

