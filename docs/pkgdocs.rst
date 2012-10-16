
================
Package Metadata
================

- **author:** Eric Hendricks

- **author-email:** eric.hendricks@nasa.gov

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.container]
    drea_wrapper.geometry.Geometry=drea_wrapper.geometry:Geometry
    drea_wrapper.stream.Stream=drea_wrapper.stream:Stream
    drea_wrapper.MEflows.MEflows=drea_wrapper.MEflows:MEflows
    drea_wrapper.DREA.DREA=drea_wrapper.DREA:DREA
    [openmdao.component]
    drea_wrapper.DREA.DREA=drea_wrapper.DREA:DREA

- **home-page:** https://github.com/OpenMDAO-Plugins/drea_wrapper

- **keywords:** openmdao

- **license:** Apache License, Version 2.0

- **maintainer:** Kenneth Moore

- **maintainer-email:** kenneth.t.moore-1@nasa.gov

- **name:** drea_wrapper

- **requires-dist:** openmdao.main

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO component wrapper for DREA

- **version:** 0.1

