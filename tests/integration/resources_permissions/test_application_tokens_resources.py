# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from taiga.base.utils import json
from tests import factories as f
from tests.utils import helper_test_http_method, disconnect_signals, reconnect_signals

from unittest import mock

import pytest
pytestmark = pytest.mark.django_db


def setup_module(module):
    disconnect_signals()


def teardown_module(module):
    reconnect_signals()


@pytest.fixture
def data():
    m = type("Models", (object,), {})
    m.registered_user = f.UserFactory.create()
    m.token = f.ApplicationTokenFactory(state="random-state")
    m.registered_user_with_token = m.token.user
    return m


def test_application_tokens_create(client, data):
    url = reverse('application-tokens-list')

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    data = json.dumps({"application": data.token.application.id})
    results = helper_test_http_method(client, "post", url, data, users)
    assert results == [405, 405, 405]


def test_applications_retrieve_token(client, data):
    url=reverse('applications-token', kwargs={"pk": data.token.application.id})

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    results = helper_test_http_method(client, "get", url, None, users)
    assert results == [401, 200, 200]


def test_application_tokens_retrieve(client, data):
    url = reverse('application-tokens-detail', kwargs={"pk": data.token.id})

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    results = helper_test_http_method(client, "get", url, None, users)
    assert results == [401, 404, 200]


def test_application_tokens_authorize(client, data):
    url=reverse('application-tokens-authorize')

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    data = json.dumps({
        "application": data.token.application.id,
        "state": "random-state-123123",
    })

    results = helper_test_http_method(client, "post", url, data, users)
    assert results == [401, 200, 200]


def test_application_tokens_validate(client, data):
    url=reverse('application-tokens-validate')

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    data = json.dumps({
        "application": data.token.application.id,
        "key": data.token.application.key,
        "auth_code": data.token.auth_code,
        "state": data.token.state
    })

    results = helper_test_http_method(client, "post", url, data, users)
    assert results == [200, 200, 200]


def test_application_tokens_update(client, data):
    url = reverse('application-tokens-detail', kwargs={"pk": data.token.id})

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    patch_data = json.dumps({"application": data.token.application.id})
    results = helper_test_http_method(client, "patch", url, patch_data, users)
    assert results == [405, 405, 405]


def test_application_tokens_delete(client, data):
    url = reverse('application-tokens-detail', kwargs={"pk": data.token.id})

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    results = helper_test_http_method(client, "delete", url, None, users)
    assert results == [401, 403, 204]


def test_application_tokens_list(client, data):
    url = reverse('application-tokens-list')

    users = [
        None,
        data.registered_user,
        data.registered_user_with_token
    ]

    results = helper_test_http_method(client, "get", url, None, users)
    assert results == [401, 200, 200]
