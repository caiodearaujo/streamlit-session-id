import os
from streamlit import experimental_get_query_params, experimental_set_query_params
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
    _set_item_comp = components.declare_component(
        "set_item",
        url="http://localhost:3305",
    )
    _clear_all_comp = components.declare_component(
        "clear_all",
        url="http://localhost:3307",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    
    start_session_build_dir = os.path.join(parent_dir, "start_session/build")
    _set_item_comp = components.declare_component("start_session", path=start_session_build_dir)

    clear_session_build_dir = os.path.join(parent_dir, "clear_session/build")    
    _clear_all_comp = components.declare_component("clear_session", path=clear_session_build_dir)

def create_session_id():
    session_id = _set_item_comp()
    experimental_set_query_params(session_id=session_id)

def has_valid_session_id_in_query_params():
    if "session_id" in experimental_get_query_params():
        if len(experimental_get_query_params().get("session_id")[0]) == 36:
            return True

def clear_all():
    _clear_all_comp()

def get_session_id():
    if not has_valid_session_id_in_query_params():
        create_session_id()
    return experimental_get_query_params().get("session_id")[0]
