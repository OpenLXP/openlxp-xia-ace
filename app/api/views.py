import logging

from celery.result import AsyncResult
from django.http import JsonResponse
from rest_framework.parsers import BaseParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
import xml.etree.ElementTree as element_Tree
from rest_framework.views import APIView

from core.tasks import execute_xia_automated_workflow

logger = logging.getLogger('dict_config_logger')


class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'application/xml'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()


# @permission_classes((permissions.AllowAny,))
class WorkflowView(APIView):
    """Handles HTTP requests for Metadata for XIS"""

    def get(self, request):
        logger.info('XIA workflow api')
        task = execute_xia_automated_workflow.delay()
        response_val = {"task_id": task.id}

        return Response(response_val, status=status.HTTP_202_ACCEPTED)


def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)


class CredentialDataView(APIView):
    """Handles HTTP requests for Credential data for XIA"""

    parser_classes = [PlainTextParser]

    def post(self, request):
        # context = self.get_context_data()
        # content_negotiation_class = IgnoreClientContentNegotiation

        # if self.kwargs.has_key('xml'):
        #     return self.render_to_response(context, content_type="text/xml; charset=utf-8")
        # return Response(self.render_to_response(context), status=status.HTTP_200_OK)

        xsr_root = element_Tree.fromstring(request.data)
        # logger.warning(xsr_root)
        # logger.warning(request.data)
        # logger.warning(type(xsr_root))
        
        xsr_items = []
        for s_item in xsr_root.findall('.//version'):
            logger.error(s_item)
            logger.info(s_item.tag, s_item.attrib)
            for item in s_item:
                logger.warning(item)
                # empty news dictionary
                logger.warning(item.attrib)
                xsr_dict = {}
                # iterate child elements of item
                for child in item:
                    xsr_dict[child.tag] = child.text
                # append xsr dictionary to xsr items list
                xsr_items.append(xsr_dict)

                for item1 in item:
                    logger.warning(item1)
                    # empty news dictionary
                    logger.warning(item1.attrib)

        # logger.error(xsr_items)
        
        
        # print(request.data)
        # print("hello")
        return Response(request.data,
                        status=status.HTTP_200_OK)
