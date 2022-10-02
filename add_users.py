from view import render_template


def create_teacher(cls):
    context = dict()
    render_template(context=context, template="add_teacher.jinja2", cls=cls)
    name = input('>> ')
    context['name'] = name

    render_template(context=context, template="add_teacher.jinja2", cls=cls)
    surname = input('>> ')
    context['surname'] = surname
    return context


def create_student(cls):
    context = dict()

    render_template(context=context, template="add_student.jinja2", cls=cls)
    name = input('>> ')
    context['name'] = name

    render_template(context=context, template="add_student.jinja2", cls=cls)
    surname = input('>> ')
    context['surname'] = surname

    render_template(context=context, template="add_student.jinja2", cls=cls)
    age = input('>> ')
    context['age'] = age

    render_template(context=context, template="add_student.jinja2", cls=cls)
    phone = input('>> ')
    context['phone'] = phone

    return context
