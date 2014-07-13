

macro(lcmtypes_get_types msgvar)
    # get a list of all LCM types
    file(GLOB __tmplcmtypes "${PROJECT_SOURCE_DIR}/lcmtypes/*.lcm")
    set(${msgvar} "")
    foreach(_msg ${__tmplcmtypes})
        # Try to filter out temporary and backup files
        if(${_msg} MATCHES "^[^\\.].*\\.lcm$")
            list(APPEND ${msgvar} ${_msg})
        endif(${_msg} MATCHES "^[^\\.].*\\.lcm$")
    endforeach(_msg)
endmacro()

function(lcmgen_for_python)
    lcmtypes_get_types(_lcmtypes)
    list(LENGTH _lcmtypes _num_lcmtypes)
    if(_num_lcmtypes EQUAL 0)
        return()
    endif()

    # generate Python bindings for LCM types
    execute_process(COMMAND ${LCM_GEN_EXECUTABLE} --lazy -p ${_lcmtypes} --ppath ${_lcmtypes_python_dir})

    # run lcm-gen at compile time
    add_custom_target(lcmgen_python ALL
        COMMAND sh -c '${LCM_GEN_EXECUTABLE} --lazy -p ${_lcmtypes} --ppath ${_lcmtypes_python_dir}')
endfunction()
