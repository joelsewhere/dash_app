# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class RadioItems(Component):
    """A RadioItems component.
RadioItems is a component that encapsulates several radio item inputs.
The values and labels of the RadioItems is specified in the `options`
property and the seleced item is specified with the `value` property.
Each radio item is rendered as an input and associated label which are
siblings of each other.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components in callbacks.
The ID needs to be unique across all of the components in an app.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info
- options (list; optional): An array of options
- value (string | number; optional): The currently selected value
- style (dict; optional): The style of the container (div)
- className (string; optional): The class of the container (div)
- inputStyle (dict; optional): The style of the <input> radio element
- inputClassName (string; default ''): The class of the <input> radio element
- labelStyle (dict; optional): Inline style arguments to apply to the <label> element for each item.
- labelCheckedStyle (dict; optional): Additional inline style arguments to apply to <label> elements on checked
items.
- labelClassName (string; default ''): CSS classes to apply to the <label> element for each item.
- labelCheckedClassName (string; optional): Additional CSS classes to apply to the <label> element when the
corresponding radio is checked.
- inline (boolean; optional): Arrange RadioItems inline
- switch (boolean; optional): Set to True to render toggle-like switches instead of radios. Ignored if
custom=False
- custom (boolean; default True): RadioItems uses custom radio buttons by default. To use native radios set
custom to False.
- loading_state (dict; optional): Object that holds the loading state object coming from dash-renderer. loading_state has the following type: dict containing keys 'is_loading', 'prop_name', 'component_name'.
Those keys have the following types:
  - is_loading (boolean; optional): Determines if the component is loading or not
  - prop_name (string; optional): Holds which property is loading
  - component_name (string; optional): Holds the name of the component that is loading"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, key=Component.UNDEFINED, options=Component.UNDEFINED, value=Component.UNDEFINED, style=Component.UNDEFINED, className=Component.UNDEFINED, inputStyle=Component.UNDEFINED, inputClassName=Component.UNDEFINED, labelStyle=Component.UNDEFINED, labelCheckedStyle=Component.UNDEFINED, labelClassName=Component.UNDEFINED, labelCheckedClassName=Component.UNDEFINED, inline=Component.UNDEFINED, switch=Component.UNDEFINED, custom=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'key', 'options', 'value', 'style', 'className', 'inputStyle', 'inputClassName', 'labelStyle', 'labelCheckedStyle', 'labelClassName', 'labelCheckedClassName', 'inline', 'switch', 'custom', 'loading_state']
        self._type = 'RadioItems'
        self._namespace = 'dash_bootstrap_components/_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'key', 'options', 'value', 'style', 'className', 'inputStyle', 'inputClassName', 'labelStyle', 'labelCheckedStyle', 'labelClassName', 'labelCheckedClassName', 'inline', 'switch', 'custom', 'loading_state']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(RadioItems, self).__init__(**args)
