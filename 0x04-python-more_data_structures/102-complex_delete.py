#!/usr/bin/python3
def complex_delete(a_dict, value):
    """Delete keys with a specific value in a dict."""
    while value in a_dict.values():
        for k, v in a_dict.items():
            if v == value:
                del a_dict[k]
                break

    return (a_dict)
