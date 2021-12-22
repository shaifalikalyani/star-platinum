from behave import given, when, then

@given(u'the url')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the url')


@when(u'I click on the icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the icon')


@when(u'I hit enter')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I hit enter')


@then(u'I get the weather updates')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get the weather updates')
