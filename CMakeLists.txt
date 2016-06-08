cmake_minimum_required(VERSION 2.6.3)

project(cogimon-gazebo-models)

file(GLOB DEPLOY_FILES_AND_DIRS "${PROJECT_SOURCE_DIR}/*")
foreach(ITEM ${DEPLOY_FILES_AND_DIRS})
   get_filename_component(tmpName ${ITEM} NAME)
   SET(fullName "${PROJECT_SOURCE_DIR}/${tmpName}")
   
   IF( IS_DIRECTORY "${ITEM}" )
      IF( NOT ((${ITEM} MATCHES "build") OR (${ITEM} MATCHES ".git")))
        message("${ITEM}")
        LIST( APPEND DIRS_TO_DEPLOY "${ITEM}" )
      ENDIF()
   ELSE()
      IF( NOT ((${ITEM} MATCHES "CMakeLists.txt") OR (${ITEM} MATCHES "README.md") OR (${ITEM} MATCHES ".gitignore")))
        LIST( APPEND FILES_TO_DEPLOY "${ITEM}" )
      ENDIF()
   ENDIF()
endforeach()

INSTALL( FILES ${FILES_TO_DEPLOY} DESTINATION "share/gazebo/models/cogimon")
INSTALL( DIRECTORY ${DIRS_TO_DEPLOY} DESTINATION "share/gazebo/models/cogimon")
