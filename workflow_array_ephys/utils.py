#!/usr/bin/env python
# coding: utf-8

# In[1]:


def convert_to_number(value: str):
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass
    return value

