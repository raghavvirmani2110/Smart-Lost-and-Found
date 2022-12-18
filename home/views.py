from django.shortcuts import redirect, render
from home.models import BkashPayment, ClaimOwner, PostModel, ResetPwdTokens, UserContact, UserFeedback, UserModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.db import connection
import time
import uuid
from lost_and_found.mail_service import send_claim_acception_mail, send_claim_rejection_mail, send_forget_password_mail, send_point_purchase_mail, send_point_success_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
# Create your views here.

# generate pdf


def pdf_generated(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        try:
            claimer = ClaimOwner.objects.raw(
                'SELECT * FROM claim_owner WHERE claimerEmail = %s and STATUS = %s;', [user.email, 'Accepted'])[0]
            showUser = UserModel.objects.get(email=claimer.postPunlisherEmail)
            post = PostModel.objects.get(id=claimer.postId)

            template_path = 'pdf_generated.html'
            context = {'user': user, 'showUser': showUser, 'post': post}
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="lost-and-found.pdf"' # for download
            response['Content-Disposition'] = 'filename="lost-and-found.pdf"'
            template = get_template(template_path)
            html = template.render(context)
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            # if error then show some funy view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except:
            messages.error(request, 'You have no pdf to show.')
            return redirect('/')
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# home function



def admin_home(request):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_posts where postStatus="Pending" ORDER BY id DESC;')
    allPosts = cursor.fetchall()
    cursor.close()
    search = "All"
    locations = []
    for post in allPosts:
        locations.append(post[5])
    locations = list(dict.fromkeys(locations))
    locations.sort()

    try:
        user = UserModel.objects.get(email=request.session['email'])
        if request.method == 'POST':
            search = request.POST.get('locatn')
            if search:
                print(search)
                if search == "All":
                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts where postType="Found" and postStatus="Pending" ORDER BY id DESC;')
                    found_posts = cursor.fetchall()
                    cursor.execute(
                        'SELECT * FROM user_posts where postType="Lost" and postStatus="Pending" ORDER BY id DESC;')
                    lost_posts = cursor.fetchall()
 
                    cursor.close()
                    return render(request, 'admin_home.html', {'lost_posts': lost_posts,'found_posts': found_posts, 'locations': locations, 'user': user, 'search': search})
                else:     

                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts WHERE location = %s and postType="Found" and postStatus="Pending" ORDER BY id DESC;', [request.POST.get('locatn')])

                    found_posts = cursor.fetchall()
                    cursor.execute(
                        'SELECT * FROM user_posts WHERE location = %s and postType="Lost" and postStatus="Pending" ORDER BY id DESC;', [request.POST.get('locatn')])
                    lost_posts = cursor.fetchall()
 
                    cursor.close()
               
                    return render(request, 'admin_home.html', {'lost_posts': lost_posts,'found_posts': found_posts, 'locations': locations, 'user': user, 'search': search})
            else:

                cursor = connection.cursor()
                cursor.execute(
                'SELECT * FROM user_posts where postType="Found" and postStatus="Pending" ORDER BY id DESC;')
                found_posts = cursor.fetchall()
                cursor.execute(
                'SELECT * FROM user_posts where postType="Lost" and postStatus="Pending" ORDER BY id DESC;')
                lost_posts = cursor.fetchall()

                cursor.close()
                return render(request, 'admin_home.html', {'lost_posts': lost_posts,'found_posts': found_posts, 'locations': locations, 'user': user, 'search': search})
        else:

            cursor = connection.cursor()
            cursor.execute(
            'SELECT * FROM user_posts where postType="Found" and postStatus="Pending" ORDER BY id DESC;')
            found_posts = cursor.fetchall()
            cursor.execute(
            'SELECT * FROM user_posts where postType="Lost" and postStatus="Pending" ORDER BY id DESC;')
            lost_posts = cursor.fetchall()
            cursor.close()
            return render(request, 'admin_home.html', {'lost_posts': lost_posts,'found_posts': found_posts, 'locations': locations, 'user': user, 'search': search})

    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

def home(request):
    try:
        if 'admin' in request.session['email']:
            return redirect('/admin-home')
    except:
        pass
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_posts ORDER BY id DESC;')
    allPosts = cursor.fetchall()
    cursor.close()
    search = "All"
    try:
        user = UserModel.objects.get(email=request.session['email'])
        if request.method == 'POST':
            search = request.POST.get('locatn')
            if search:
                print(search)
                if search == "All":
                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts ORDER BY id DESC;')
                    posts = cursor.fetchall()
                    cursor.close()
                    locations = []
                    for post in allPosts:
                        locations.append(post[5])
                    locations = list(dict.fromkeys(locations))
                    locations.sort()
                    return render(request, 'home.html', {'posts': posts, 'locations': locations, 'user': user, 'search': search})
                else:
                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts WHERE location = %s ORDER BY id DESC;', [search])
                    posts = cursor.fetchall()
                    cursor.close()
                    locations = []
                    for post in allPosts:
                        locations.append(post[5])
                    locations = list(dict.fromkeys(locations))
                    locations.sort()
                    return render(request, 'home.html', {'posts': posts, 'locations': locations, 'user': user, 'search': search})
            else:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM user_posts ORDER BY id DESC;')
                posts = cursor.fetchall()
                cursor.close()
                locations = []
                for post in allPosts:
                    locations.append(post[5])
                locations = list(dict.fromkeys(locations))
                locations.sort()
                return render(request, 'home.html', {'posts': posts, 'locations': locations, 'user': user, 'search': search})
        else:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM user_posts ORDER BY id DESC;')
            posts = cursor.fetchall()
            cursor.close()
            locations = []
            for post in allPosts:
                locations.append(post[5])
            locations = list(dict.fromkeys(locations))
            locations.sort()
            return render(request, 'home.html', {'posts': posts, 'locations': locations, 'user': user, 'search': search})
    except:
        if request.method == 'POST':
            search = request.POST.get('locatn')
            if search:
                print(search)
                if search == "All":
                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts ORDER BY id DESC;')
                    posts = cursor.fetchall()
                    cursor.close()
                    locations = []
                    for post in allPosts:
                        locations.append(post[5])
                    locations = list(dict.fromkeys(locations))
                    locations.sort()
                    return render(request, 'home.html', {'posts': posts, 'locations': locations, 'search': search})
                else:
                    cursor = connection.cursor()
                    cursor.execute(
                        'SELECT * FROM user_posts WHERE location = %s ORDER BY id DESC;', [request.POST.get('locatn')])
                    posts = cursor.fetchall()
                    cursor.close()
                    locations = []
                    for post in allPosts:
                        locations.append(post[5])
                    locations = list(dict.fromkeys(locations))
                    locations.sort()
                    return render(request, 'home.html', {'posts': posts, 'locations': locations, 'search': search})
            else:
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM user_posts ORDER BY id DESC;')
                posts = cursor.fetchall()
                cursor.close()
                locations = []
                for post in allPosts:
                    locations.append(post[5])
                locations = list(dict.fromkeys(locations))
                locations.sort()
                return render(request, 'home.html', {'posts': posts, 'locations': locations, 'search': search})
        else:
            cursor = connection.cursor()
            cursor.execute(
                'SELECT * FROM user_posts ORDER BY id DESC;')
            posts = cursor.fetchall()
            cursor.close()
            locations = []
            for post in allPosts:
                locations.append(post[5])
            locations = list(dict.fromkeys(locations))
            locations.sort()
            return render(request, 'home.html', {'posts': posts, 'locations': locations, 'search': search})


# authentication function

def authenticate(request):
    return render(request, 'authenticate.html')


# admin login function

def admin_login(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        if request.method == 'POST':
            if request.POST.get('adminUsername') and request.POST.get('adminPass'):
                username = request.POST.get('adminUsername')
                password = request.POST.get('adminPass')
                if username == 'admin' and password == 'admin':
                    return redirect('admin-panel')
                else:
                    messages.error(request, 'Password incorrect...!')
                    return render(request, 'admin_login.html', {'user': user})
        return render(request, 'admin_login.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# admin panel function


def admin_panel(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])

        pendings = BkashPayment.objects.raw(
            'SELECT * FROM bkash_payment WHERE STATUS = %s', ['Pending'])
        users = UserModel.objects.raw(
            'SELECT * FROM app_users WHERE email != %s', [request.session['email']])

        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM claim_owner co, user_posts up WHERE co.postId = up.id and co.STATUS = %s ORDER BY co.id ASC;', ['Pending'])
        claims = cursor.fetchall()
        cursor.close()


        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM user_posts ORDER BY id DESC;')
        posts = cursor.fetchall()
        cursor.close()
        locations = []
        for post in posts:
            locations.append(post[5])
        locations = list(dict.fromkeys(locations))
        locations.sort()
        
        return render(request, 'admin_panel.html', {'user': user, 'pendings': pendings, 'claims': claims, 'users': users,'posts': posts, 'locations': locations, 'user': user, 'search': 'ALL'})
        # else:
        #     messages.error(request, "Restricted! Only admin users can access.")
        #     return redirect('/', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# point add function (Admin Panel)


def point_add(request, token):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM app_users au, bkash_payment bp WHERE au.email = bp.email and bp.id = %s ORDER BY bp.id DESC', [token])

    puser = cursor.fetchall()
    cursor.close()
    try:
        user = UserModel.objects.get(email=request.session['email'])

        if user.email == 'admin':

            tuser = UserModel.objects.get(email=puser[0][18])

            tuser.point = str(int(tuser.point) + int(puser[0][21]))
            tuser.save()

            pend = BkashPayment.objects.get(id=token)
            pend.status = "Done"
            pend.save()

            send_point_success_mail(puser[0][18])

            messages.success(request, "Point added to " +
                             puser[0][17] + " user successfully.")
            return redirect('/admin-panel', {'user': user})
        else:
            messages.error(request, "Restricted! Only admin users can access.")
            return redirect('/', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login')


# signup function

def signup(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('password'):
            saveUser = UserModel()
            saveToken = ResetPwdTokens()

            saveUser.name = request.POST.get('name')
            saveUser.email = request.POST.get('email')
            saveUser.password = make_password(request.POST.get('password'))
            saveUser.completeProfile = '25%'
            saveUser.point = '200'

            if saveUser.isExists():
                messages.error(
                    request, request.POST.get('email') + " email address already registered...! Please Log in.")
                # return render(request, 'authenticate.html', context)
                return redirect('../authenticate')
            else:
                saveUser.save()
                saveToken.user = saveUser
                saveToken.save()
                messages.success(
                    request, "Hello " + request.POST.get('name') + ", registration details saved successfully...! Please Log in now.")
                return redirect('../authenticate')
    else:
        return redirect('../authenticate')


# login function

def login(request):
    if request.method == 'POST':
        try:
            userDetail = UserModel.objects.get(
                email=request.POST.get('email'))
            if check_password(request.POST.get('password'), (userDetail.password)):
                request.session['email'] = userDetail.email
                if 'admin' in request.POST.get('email') and 'admin' in request.POST.get('password'):
                    return redirect('/admin-home')
                else:
                    return redirect('/')
            else:
                messages.error(
                    request, 'Password incorrect...!')
        except UserModel.DoesNotExist as e:
            messages.error(
                request, 'No user found of this email....!')
    return redirect('../authenticate')


# logout function

def logout(request):
    try:
        del request.session['email']
        messages.success(request, "Successfully logged out.")
    except:
        messages.error(request, "An error occurred. Try again.")
        return redirect('/')
    return redirect('/')


# privacy policy function

def privacy_policy(request):
    return render(request, 'privacy_policy.html')


# terms & conditions function

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

# view profile page

def view_claimed(request):

    try:
        if 'admin' in request.session['email']:

            all_claimed = ClaimOwner.objects.all()
            print(all_claimed)
            return render(request, 'view_claimed.html',{'all_claimed':all_claimed})
    except Exception as e:
        print(e)
        messages.error(request, 'You need to login first')
        return redirect('authenticate')


def view_profile(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        return render(request, 'view_profile.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# edit profile page


def edit_profile(request):
    if request.method == 'POST':
        user = UserModel.objects.get(email=request.session['email'])
        if request.POST.get('editName') and request.POST.get('editPhn') and request.POST.get('editLocation') and request.POST.get('editBio') and request.POST.get('editMessengerUrl') and request.POST.get('editWhatsappUrl'):

            user.name = request.POST.get('editName')
            user.phoneNumber = request.POST.get('editPhn')
            user.location = request.POST.get('editLocation')
            user.bio = request.POST.get('editBio')
            user.messengerUrl = request.POST.get('editMessengerUrl')
            user.whatsappUrl = request.POST.get('editWhatsappUrl')
            if request.POST.get('editTelegramUrl'):
                user.telegramUrl = request.POST.get('editTelegramUrl')
            user.completeProfile = '100%'

            # TODO: single photo file save
            if len(request.FILES) != 0:
                user.profileImg = request.FILES['editPhoto']
                user.nidFrontImg = request.FILES['editNidFront']
                user.nidBackImg = request.FILES['editNidBack']

            user.save()
            messages.success(
                request, "Your profile updated successfully...!")
            return redirect('view-profile')

    else:
        try:
            user = UserModel.objects.get(email=request.session['email'])
            return render(request, 'edit_profile.html', {'user': user})
        except:
            messages.error(request, 'You need to login first')
            return redirect('authenticate')

# contact function


def contact(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])

        if request.method == 'POST':
            if request.POST.get('txtname') and request.POST.get('txtEmail') and request.POST.get('txtMsg'):
                saveContact = UserContact()

                saveContact.messengerId = user.id
                saveContact.messengerName = user.name
                saveContact.messengerEmail = user.email
                saveContact.message = request.POST.get('txtMsg')

                saveContact.save()
                time.sleep(3)
                return redirect('/')
        else:
            return render(request, 'contact.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# feedback functon


def feedback(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        if request.method == 'POST':
            if request.POST.get('feedbackMsg'):
                saveFeedback = UserFeedback()

                saveFeedback.messengerId = user.id
                saveFeedback.messengerName = user.name
                saveFeedback.messengerEmail = user.email
                saveFeedback.message = request.POST.get('feedbackMsg')

                saveFeedback.save()
                return redirect('/')
        else:
            return render(request, 'feedback.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# reset password functon


def forget_password(request):
    try:
        if request.method == 'POST' and request.POST.get('resetEmail'):
            email = request.POST.get('resetEmail')

        if not UserModel.objects.filter(email=email).first():
            messages.error(request, 'No user found with this email.')
            return render(request, 'reset_password/forget-password.html')

        user_obj = UserModel.objects.get(email=email)
        token = str(uuid.uuid4())
        resetPwdToken_obj = ResetPwdTokens.objects.get(user=user_obj.id)
        resetPwdToken_obj.forget_password_token = token
        resetPwdToken_obj.save()
        send_forget_password_mail(user_obj.email, token)
        messages.success(request, 'An email has been sent to ' + user_obj.email +
                         '. If you don\'t find any email in your mailbox, please check spam folder.')
        return render(request, 'reset_password/forget-password.html')

    except Exception as e:
        print(e)
    return render(request, 'reset_password/forget-password.html')

# change password functon


def change_password(request, token):
    context = {}

    try:
        resetPwdToken_obj = ResetPwdTokens.objects.filter(
            forget_password_token=token).first()
        context = {'user_id': resetPwdToken_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.error(request, 'No user id found.')
                return render(request, f'reset_password/change-password/{token}/.html', context)

            if new_password != confirm_password:
                messages.error(request, 'both should be equal.')
                return render(request, f'reset_password/change-password/{token}/.html', context)

            user_obj = UserModel.objects.filter(id=user_id).first()
            user_obj.password = make_password(new_password)
            user_obj.save()
            messages.success(request, 'Password updated.')
            return render(request, 'reset_password/change-password.html', context)
        else:
            return render(request, 'reset_password/change-password.html', context)

    except Exception as e:
        print(e)
        messages.error(request, 'url has already been used.')
        return render(request, 'reset_password/change-password.html', context)

# write post function


def write_post(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        if user.completeProfile == '100%':
            if request.method == 'POST':
                if request.POST.get('title') and request.POST.get('location') and request.POST.get('description') and request.POST.get('datetime'):

                    savePost = PostModel()

                    savePost.publisherId = user.id
                    savePost.publisherName = user.name
                    savePost.title = request.POST.get('title')
                    savePost.description = request.POST.get('description')
                    savePost.location = request.POST.get('location')
                    savePost.lostDateTime = request.POST.get('datetime')
                    savePost.postType = "Found"

                    if len(request.FILES) != 0:
                        savePost.fileImg = request.FILES['fileImg']
                        savePost.fileSecretImg = request.FILES['fileSecretImg']

                    user.point = str(int(user.point) + 50)

                    user.save()
                    savePost.save()

                    messages.success(request, "Your post has been submitted!")
                    return redirect('/')
            else:
                return render(request, 'write_post.html', {'user': user})
        else:
            messages.error(request, "Complete your profile first!")
            return render(request, 'view_profile.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')

# edit post function


def req_post(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        if user.completeProfile == '100%':
            if request.method == 'POST':
                if request.POST.get('title') and request.POST.get('location') and request.POST.get('description') and request.POST.get('datetime'):

                    savePost = PostModel()

                    savePost.publisherId = user.id
                    savePost.publisherName = user.name
                    savePost.title = request.POST.get('title')
                    savePost.description = request.POST.get('description')
                    savePost.location = request.POST.get('location')
                    savePost.lostDateTime = request.POST.get('datetime')
                    savePost.postType = "Lost"

                    if len(request.FILES) != 0:
                        savePost.fileImg = request.FILES['fileImg']
                        savePost.fileSecretImg = request.FILES['fileSecretImg']

                    user.point = str(int(user.point) - 50)

                    user.save()
                    savePost.save()

                    messages.success(request, "Your post has been submitted!")
                    return redirect('/')
            else:
                return render(request, 'req_post.html', {'user': user})
        else:
            messages.error(request, "Complete your profile first!")
            return render(request, 'view_profile.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')


def edit_post(request, token):
    try:
        user = UserModel.objects.get(email=request.session['email'])
        post = PostModel.objects.get(id=token)
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('location') and request.POST.get('description'):

                post.publisherId = user.id
                post.publisherName = user.name
                post.title = request.POST.get('title')
                post.description = request.POST.get('description')
                post.location = request.POST.get('location')

                post.save()

                messages.success(request, "Your post has been edited!")
                return redirect('/')
        else:
            return render(request, 'edit_post.html', {'user': user, 'post': post})
    except:
        messages.error(request, 'You need to login first')
        return redirect('authenticate')


import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('corpus')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import imgcompare
import PIL.Image as Image
def getSim(X,Y):
    
    X = X.lower() 
    Y = Y.lower() 
    
    X_list = word_tokenize(X)  
    Y_list = word_tokenize(Y) 
    
    sw = stopwords.words('english')  
    l1 =[];l2 =[] 
    
    X_set = {w for w in X_list if not w in sw}  
    Y_set = {w for w in Y_list if not w in sw} 
        
    rvector = X_set.union(Y_set)  
    for w in rvector: 
        if w in X_set: l1.append(1)
        else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0) 
    c = 0
        
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 

    return cosine*100

    


def view_post(request, token):
    type_post = ""
    similar_posts = []
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM app_users au, user_posts up WHERE au.id = up.publisherId and up.id = %s', [token])
    posts = cursor.fetchall()


    cursor.execute(
        'SELECT * FROM user_posts up WHERE id = %s', [token])

    curr_post = cursor.fetchall()[0]


    if curr_post[10]=="Lost":
        type_post = "All founded items by other users"
        
        cursor.execute(
            'SELECT * FROM user_posts WHERE postType="Found" and postStatus="Pending" ORDER BY id DESC;')

        found_posts = cursor.fetchall()
        for one_post in found_posts:
            
            image_a = Image.open(one_post[7]).resize((500,500)).convert('LA')
            image_b = Image.open(curr_post[7]).resize((500,500)).convert('LA')
            img_percentage = float("{:.2f}".format( 100 - imgcompare.image_diff_percent(image_a, image_b)))
            score=float("{:.2f}".format(getSim(one_post[3]+" " +one_post[4],curr_post[3]+" " +curr_post[4])))

            cursor.execute(
                "SELECT * FROM app_users WHERE id='"+one_post[1]+"';")
            publisher = cursor.fetchall()[0]

            similar_posts.append({                
                'text_sim':score,
                'img_sim':img_percentage,
                'cur_id':curr_post[0], 'cur_publisherId':curr_post[1], 'cur_title':curr_post[3], 'cur_location':curr_post[5], 'cur_postType':curr_post[10],            
            'post_id':one_post[0], 'post_publisherId':one_post[1], 'post_publisherName':one_post[2], 'post_title':one_post[3], 'post_description':one_post[4], 'post_location':one_post[5], 'post_lostDateTime':one_post[6], 'post_fileImg':one_post[7], 'post_fileSecretImg':one_post[8], 'post_created_at':one_post[9], 'post_postType':one_post[10],
            'name':publisher[1], 'publisher_email':publisher[2], 'publisher_phoneNumber':publisher[4], 'publisher_profileImg':publisher[12]
            
            })

    else:

        type_post = "All loosted items by other users"

        cursor.execute(
            'SELECT * FROM user_posts WHERE postType="Lost" and postStatus="Pending" ORDER BY id DESC;')

        lost_posts = cursor.fetchall()
        for one_post in lost_posts:
           
            image_a = Image.open(one_post[7]).resize((500,500)).convert('LA')
            image_b = Image.open(curr_post[7]).resize((500,500)).convert('LA')
            img_percentage = float("{:.2f}".format(100- imgcompare.image_diff_percent(image_a, image_b)))
            score=float("{:.2f}".format(getSim(one_post[3]+" " +one_post[4],curr_post[3]+" " +curr_post[4])))
        
            cursor.execute(
                "SELECT * FROM app_users WHERE id='"+one_post[1]+"';")
            publisher = cursor.fetchall()[0]

            similar_posts.append({                
                'text_sim':score,
                'img_sim':img_percentage,
                    'cur_id':curr_post[0], 'cur_publisherId':curr_post[1], 'cur_title':curr_post[3], 'cur_location':curr_post[5], 'cur_postType':curr_post[10],            
            'post_id':one_post[0], 'post_publisherId':one_post[1], 'post_publisherName':one_post[2], 'post_title':one_post[3], 'post_description':one_post[4], 'post_location':one_post[5], 'post_lostDateTime':one_post[6], 'post_fileImg':one_post[7], 'post_fileSecretImg':one_post[8], 'post_created_at':one_post[9], 'post_postType':one_post[10],
            'name':publisher[1], 'publisher_email':publisher[2], 'publisher_phoneNumber':publisher[4], 'publisher_profileImg':publisher[12]

            })



    cursor.close()

    try:
        user = UserModel.objects.get(email=request.session['email'])
        return render(request, 'view_post.html', {'posts': posts, 'user': user,'similar_posts':similar_posts,'type_post':type_post})
    except:
        return render(request, 'view_post.html', {'posts': posts,'type_post':type_post})

# claim owner function


def claim_owner(request, token):
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM app_users au, user_posts up WHERE au.id = up.publisherId and up.id = %s', [token])
    posts = cursor.fetchall()
    cursor.close()
    try:
        user = UserModel.objects.get(email=request.session['email'])

        if user.completeProfile == '100%':

            claimOwner = ClaimOwner()

            claimOwner.claimerId = user.id
            claimOwner.claimerName = user.name
            claimOwner.claimerEmail = user.email
            claimOwner.postId = token
            claimOwner.postPunlisherEmail = posts[0][2]
            claimOwner.postPunlisherName = posts[0][18]
            claimOwner.status = 'Pending'

            if len(request.FILES) != 0:
                claimOwner.claimFileImg = request.FILES['secretPic']

            claimOwner.save()

            user.point = str(int(user.point) - 100)
            user.save()

            messages.success(
                request, "Your claim has been submitted! You will get updates through email.")
            return redirect('/')
        else:
            messages.error(request, "Complete your profile first!")
            return render(request, 'view_profile.html', {'user': user})
    except:
        messages.error(
            request, "Something went wrong. Please try again later.")
        return redirect('/')



def claim_accept(request,  curr_PostId, clicked_PostId,type_post):
    try:

        cursor = connection.cursor()
        lost_user = None
        found_user = None
        losted_posts = None
        found_posts = None

        if "loosted" in type_post:

            cursor.execute(
                'SELECT * FROM user_posts where id = %s', [curr_PostId])
            losted_posts = cursor.fetchall()[0]

            print("\n\nClaimer(Who Lost)\n\n",'\n\n',losted_posts)
            
            cursor.execute(
                'SELECT * FROM app_users where id = %s', [losted_posts[1]])
            lost_user = cursor.fetchall()[0]
            
            cursor.execute(
                'SELECT * FROM user_posts where id = %s', [clicked_PostId])
            found_posts = cursor.fetchall()[0]

            print("\n\nPoster(Who Found)\n\n",'\n\n',found_posts)

            cursor.execute(
                'SELECT * FROM app_users where id = %s', [found_posts[1]])
            found_user = cursor.fetchall()[0]

        else:

            cursor.execute(
                'SELECT * FROM user_posts where id = %s', [clicked_PostId])
            losted_posts = cursor.fetchall()[0]

            print("\n\nClaimer(Who Lost)\n\n",'\n\n',losted_posts)
            
            cursor.execute(
                'SELECT * FROM app_users where id = %s', [losted_posts[1]])
            lost_user = cursor.fetchall()[0]
            

            cursor.execute(
                'SELECT * FROM user_posts where id = %s', [curr_PostId])
            found_posts = cursor.fetchall()[0]

            print("\n\nPoster(Who Found)\n\n",'\n\n',found_posts)

            cursor.execute(
                'SELECT * FROM app_users where id = %s', [found_posts[1]])
            found_user = cursor.fetchall()[0]


        send_claim_acception_mail( found_user,lost_user[2])


        claimOwner = ClaimOwner()
        
        claimOwner.lostPostId = losted_posts[0]
        claimOwner.lostPostUserId = losted_posts[1]
        claimOwner.lostPostUserName = losted_posts[2]
        claimOwner.lostPostUserEmail = lost_user[2]
        claimOwner.lostPostTittle = losted_posts[3]
        claimOwner.lostPostDescription = losted_posts[4]
        claimOwner.lostPostImg = losted_posts[7]

        claimOwner.foundPostId = found_posts[0]
        claimOwner.foundPostUserId = found_posts[1]
        claimOwner.foundPostUserName = found_posts[2]
        claimOwner.foundPostUserEmail = found_user[2]
        claimOwner.foundPostTittle = found_posts[3]
        claimOwner.foundPostDescription = found_posts[4]
        claimOwner.foundPostImg = found_posts[7]

        claimOwner.status = 'Claimed'
        claimOwner.save()

        cursor.execute("UPDATE user_posts SET postStatus='Claimed' where id = '"+str(losted_posts[0])+"' ;")
        cursor.execute("UPDATE user_posts SET postStatus='Claimed' where id = '"+str(found_posts[0])+"' ;")
        cursor.close()

        messages.success(request, "Claim has been accepted!")
        return redirect('admin-home')
    except:
        messages.error(
            request, "Something went wrong. Please try again later.")
        return redirect('/')

# claim owner REJECTION function


def claim_reject(request, token):
    try:
        claimOwner = ClaimOwner.objects.get(id=token)
        claimOwner.status = 'Rejected'
        claimOwner.save()

        send_claim_rejection_mail(claimOwner.claimerEmail)

        messages.success(request, "Claim has been rejected!")
        return redirect('admin-panel')
    except:
        messages.error(
            request, "Something went wrong. Please try again later.")
        return redirect('/')


def point_purchase(request):
    try:
        user = UserModel.objects.get(email=request.session['email'])

        if request.method == 'POST':
            if request.POST.get('inputName') and request.POST.get('inputEmail') and request.POST.get('bkashNumber') and request.POST.get('bkashTransaction') and request.POST.get('inputPoint'):

                savePayment = BkashPayment()

                savePayment.name = request.POST.get('inputName')
                savePayment.email = request.POST.get('inputEmail')
                savePayment.status = 'Pending'
                savePayment.bkashNumber = request.POST.get('bkashNumber')
                savePayment.bkashTransaction = request.POST.get(
                    'bkashTransaction')
                savePayment.point = request.POST.get('inputPoint')

                savePayment.save()
                send_point_purchase_mail(request.POST.get('inputName'))
                messages.success(
                    request, "Your point purchase request has been submitted. We will confirm you by email within an hour.")
                return render(request, 'point-purchase.html', {'user': user})
        else:
            return render(request, 'point-purchase.html', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login')

