from django import template
from django.utils.safestring import mark_safe
from django.conf import settings

register = template.Library()


@register.filter
def cascade_select(value):
    response_url = value.pop()
    mochikit_src = """
<script src= "/static/js/MochiKit/MochiKit.js" type="text/javascript"></script>
"""
    script_output = u"""
<script type="text/javascript">
function on_succeed_callback_%(event_element)s(res){
    filter_element = MochiKit.DOM.getElement('id_%(filter_element)s');
    filter_element.parentNode.innerHTML = res.responseText;
    if (select_changed_%(filter_element)s){
        filter_element = MochiKit.DOM.getElement('id_%(filter_element)s');
        MochiKit.Signal.connect(filter_element, "onchange", select_changed_%(filter_element)s);
    }
}

function select_changed_%(event_element)s(eventObj){
    target = eventObj.target();
    d = MochiKit.Async.doSimpleXMLHttpRequest('%(response_url)s',{ '%(event_element)s': target.value } );
    d.addCallback(on_succeed_callback_%(event_element)s); 
} 
event_element = MochiKit.DOM.getElement('id_%(event_element)s');
MochiKit.Signal.connect(event_element, "onchange", select_changed_%(event_element)s); 
</script>
"""
    output = [mochikit_src]
    for event_element, filter_element, event_model, filter_model in value:
        output.append(script_output % {'event_element': event_element, 'filter_element': filter_element,
                                       'response_url': response_url})
    return mark_safe(u''.join(output))


cascade_select.is_safe = True