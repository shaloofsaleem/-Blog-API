from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q




class PublicBlogView(APIView):
     def get(self, request):
        try:
            
            blog = Blog.objects.all().order_by('?')
            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = Blog.objects.filter(Q(title__icontains =search)|Q(blog_text__icontains = search))
            page_number = request.GET.get('page', 1)
            pagiantor = pagiantor(blog , 5)
            serializer= BlogSerializer(pagiantor.page(page_number),many = True)
            
            
            return Response({
                    'data':serializer.data,
                    'message': 'Blog fatched Successfully'
            },status= status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                    'data':{},
                    'message': 'something went wrong and invalide page'
                },status= status.HTTP_400_BAD_REQUEST)    
    

class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        try:
            blog = Blog.objects.filter(user = request.user)
            if request.GET.get('search'):
                search = request.GET.get('search')
                blog = Blog.objects.filter(Q(title__icontains =search)|Q(blog_text__icontains = search))
            serializer = BlogSerializer(blog , many =True)
            return Response({
                    'data':serializer.data,
                    'message': 'Blog fatched Successfully'
            },status= status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                    'data':{},
                    'message': 'something went wrong'
                },status= status.HTTP_400_BAD_REQUEST)    
    def post(self, request):
        try :
            data = request.data
            data['user']= request.user.id
            # print("#########################")
            # print(request.user)
            # print("#########################")
            serializer = BlogSerializer(data= data)
            if not serializer.is_valid():
                 return Response({
                    'data':serializer.errors,
                    'message': 'something went wrong'   
                },status= status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response({
                    'data':serializer.data,
                    'message': 'Blog Created Successfully'
            },status= status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    'data':{},
                    'message': 'something went wrong'
                },status= status.HTTP_400_BAD_REQUEST)


    def patch (self,request):
        try :
            data = request.data
            blog = Blog.objects.filter(uid = data.get('uid'))
            
            if not blog.exists():
                return Response({
                    'data':{},
                    'message': 'Invalid blog uid'
                },status= status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog[0].user:
                return Response({
                    'data':{},
                    'message': 'you are not outharized to this'
                },status= status.HTTP_400_BAD_REQUEST)
            
            serializer= BlogSerializer(instance=blog[0],data=data, partial = True)
            
            if not serializer.is_valid():
                print('fgdfhdfhgf',serializer.errors)
                return Response({
                'data':serializer.errors,
                'message': 'something went wrong'   
            },status= status.HTTP_400_BAD_REQUEST)
            serializer.save()
            
            return Response({
                    'data':serializer.data,
                    'message': 'Blog Update Successfully'
            },status= status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    'data':{},
                    'message': 'something went wrong'
                },status= status.HTTP_400_BAD_REQUEST)  
            
   
                
                
    def  delete (self,request):
        try :
            data = request.data
            blog = Blog.objects.filter(uid = data.get('uid'))
            
            if not blog.exists():
                return Response({
                    'data':{},
                    'message': 'Invalid blog uid'
                },status= status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog[0].user:
                return Response({
                    'data':{},
                    'message': 'you are not outharized to this'
                },status= status.HTTP_400_BAD_REQUEST)
                
            blog[0].delete()
            
            return Response({
                    'data':{},
                    'message': 'Blog deleted Successfully'
            },status= status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                    'data':{},
                    'message': 'something went wrong'
                },status= status.HTTP_400_BAD_REQUEST)  
                
            
            
                
            
    
                