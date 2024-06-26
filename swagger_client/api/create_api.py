# coding: utf-8

"""
    Rush Analytics API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    Contact: support@rushanalytics.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CreateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_ad_words_project(self, body, **kwargs):  # noqa: E501
        """Create AdWords parsing project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ad_words_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdWordsParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_ad_words_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_ad_words_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_ad_words_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create AdWords parsing project  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_ad_words_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AdWordsParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ad_words_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_ad_words_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/adwords', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_fpp_project(self, body, **kwargs):  # noqa: E501
        """Create Fast Positions parsing project  # noqa: E501

        At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fpp_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFpp body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_fpp_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_fpp_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_fpp_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Fast Positions parsing project  # noqa: E501

        At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fpp_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateFpp body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_fpp_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_fpp_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/fpp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_indexation_project(self, body, **kwargs):  # noqa: E501
        """Create Indexation parsing project  # noqa: E501

        At least one searchEngine is required. At least one keyword is required.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_indexation_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndexationParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_indexation_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_indexation_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_indexation_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Indexation parsing project  # noqa: E501

        At least one searchEngine is required. At least one keyword is required.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_indexation_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IndexationParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_indexation_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_indexation_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/indexation', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_rpp_project(self, body, **kwargs):  # noqa: E501
        """Create Rank Tracker project BETA  # noqa: E501

        At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_rpp_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRpp body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_rpp_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_rpp_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_rpp_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Rank Tracker project BETA  # noqa: E501

        At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_rpp_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRpp body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_rpp_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_rpp_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/ranktracker', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_suggest_project(self, body, **kwargs):  # noqa: E501
        """Create Suggest parsing project  # noqa: E501

        At least one region type is required. Depth can be 1-3.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_suggest_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SuggestParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_suggest_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_suggest_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_suggest_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Suggest parsing project  # noqa: E501

        At least one region type is required. Depth can be 1-3.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_suggest_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SuggestParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_suggest_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_suggest_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/suggest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_top10_project(self, body, **kwargs):  # noqa: E501
        """Create Top 10 parsing project  # noqa: E501

        At least one keyword is required. Depth is optional parameter and can be 10-100, automatically rounded to next 10. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_top10_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Top10Parameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_top10_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_top10_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_top10_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Top 10 parsing project  # noqa: E501

        At least one keyword is required. Depth is optional parameter and can be 10-100, automatically rounded to next 10. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_top10_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Top10Parameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_top10_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_top10_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/top10', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_wordstat_project(self, body, **kwargs):  # noqa: E501
        """Create Wordstat parsing project  # noqa: E501

        Valid inputs for pages are 1-10, maximum pages are collected if input is not specified or out of range. 'pages' parameter is valid for 'Keywords' project type. 'normal', 'parentheses', 'exclamation' and 'wordorder' parameters are valid for type 'SearchVolume'. 'minimumwordstat' is optional, defaults to 1.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wordstat_project(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WordstatParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_wordstat_project_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_wordstat_project_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_wordstat_project_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Wordstat parsing project  # noqa: E501

        Valid inputs for pages are 1-10, maximum pages are collected if input is not specified or out of range. 'pages' parameter is valid for 'Keywords' project type. 'normal', 'parentheses', 'exclamation' and 'wordorder' parameters are valid for type 'SearchVolume'. 'minimumwordstat' is optional, defaults to 1.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_wordstat_project_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WordstatParameters body: Project parameters (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_wordstat_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_wordstat_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/create/wordstat', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
