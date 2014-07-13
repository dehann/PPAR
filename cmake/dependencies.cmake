
macro(check_for_python)
    find_package(PythonInterp)
    if(NOT PYTHONINTERP_FOUND)
        message(STATUS "Not building Python LCM type bindings (Can't find Python)")
        return()
    endif()
endmacro()


