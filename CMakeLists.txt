cmake_minimum_required(VERSION 2.8.7)

set(CMAKE_INSTALL_PREFIX ${PROJECT_SOURCE_DIR}/build)

# pull in the pods macros. See cmake/pods.cmake for documentation
set(PROJECT_NAME ppar)
#include(cmake/pods.cmake) -- moving away from the pods build system

# automatically build LCM types. This also defines a number of CMake
# variables, see cmake/lcmtypes.cmake for details
include(cmake/dependencies.cmake)
include(cmake/lcm-general.cmake)

check_for_python()

# this may be duplicating cmake functions
set(_lcmtypes_install_dir ${PROJECT_SOURCE_DIR}/build/include/lcmtypes/)
execute_process(COMMAND mkdir -p ${_lcmtypes_install_dir})
#execute_process(COMMAND mkdir -p ${CMAKE_BINARY_DIR}/bin)

#set(${TARGET_DIR} )

# call lcm-gen and install to _lcm_python_dir defined above..
gen_python_lcmtypes()

install(FILES ${python_files} DESTINATION bin)


