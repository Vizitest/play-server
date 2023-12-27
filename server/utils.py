from server.app import app
from server.constants import CONTENT_TYPE_HTML


def make_user_filter(name, surname):
    def filter_function(pair):
        key, user = pair
        if name is not None and surname is not None:
            return user['name'] == name and user['surname'] == surname
        elif name is not None:
            return user['name'] == name
        elif surname is not None:
            return user['surname'] == surname
        else:
            return True

    return filter_function


def build_api_info():
    from werkzeug.utils import import_string
    def format_rule(rule, doc):
        import urllib.parse
        from html import escape
        def build_li(x):
            escaped_item = escape(x)
            import re
            escaped_item = re.sub(r'&gt;', "</i>&gt;", re.sub(r'&lt;', '&lt;<i>', escaped_item))
            return f"<li>{escaped_item}</li>"

        method_info = "".join(map(build_li, rule.methods))
        documentation = "" if doc is None else escape(doc)
        return f"""<li><dl>
                                <dt>{escape(urllib.parse.unquote(rule.rule))}</dt>
                                <dd>
                                <dl>
                                <dt>Methods</dt>
                                <dd>
                                <ul>
                                {method_info}
                                </ul>
                                </dd>
                                <dt>Doc</dt>
                                <dd><code><pre>{documentation}</pre></code></dd>
                                </dl>
                                </dd>
                                </dl></li>"""

    routes = []
    for rule in app.url_map.iter_rules():
        try:
            if rule.endpoint != 'static':
                if hasattr(app.view_functions[rule.endpoint], 'import_name'):
                    import_name = app.view_functions[rule.endpoint].import_name
                    obj = import_string(import_name)
                    routes.append(format_rule(rule, obj.__doc__))
                else:
                    routes.append(format_rule(rule, app.view_functions[rule.endpoint].__doc__))
        except Exception as exc:
            route_info = "%s => %s" % (rule.rule, rule.endpoint)
            app.logger.error("Invalid route: %s" % route_info, exc_info=True)
            # func_list[rule.rule] = obj.__doc__
    all_routes = "".join(routes)
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
    <title>API Test Server Documentation</title>
    <meta charset="UTF-8">
    </head>
    <body>
    <h1>API Test Server Documentation</h1>
    <h2>General Info</h2>
        <p>Please note: <i>namespace</i> can be anything,
         if it does not exist, it will be created, and a reset will zap it out of existence.</p>
         <h2>Route Info</h2>
         <ul>{all_routes}</ul>
        </body>
        </html>""", 200, CONTENT_TYPE_HTML
