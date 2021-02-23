from django import template
register = template.Library()


class SetVarNode(template.Node):

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def render(self, context):
        try:
            value = template.Variable(self.value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.name] = value
        return ""


@register.tag(name='set')
def set_var(parser, token):
    """
    {% set some_var = '123' %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <name> = <value> %}")
    return SetVarNode(parts[1], parts[3])
