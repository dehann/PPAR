
set(LCM_GEN_EXECUTABLE lcm-gen)

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

function(gen_python_lcmtypes)
    lcmtypes_get_types(_lcmtypes)
    list(LENGTH _lcmtypes _num_lcmtypes)
    if(_num_lcmtypes EQUAL 0)
        return()
    endif()

    # run lcm-gen at compile time
    add_custom_target(lcmgen_python ALL
        COMMAND sh -c '${LCM_GEN_EXECUTABLE} --lazy -p ${_lcmtypes} --ppath ${_lcmtypes_install_dir}')
endfunction()
