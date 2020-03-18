from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Posts
from application.forms import PostForm, UpdateAccountForm


@app.route('/')
@app.route('/home')
def home():
    outfitData = outfitid.query.all()
    return render_template('home.html', title='Home', outfitData=outfitData)

@app.route('/about')
def about():
    return render_template('about.html' , title='About')
@app.route('/register', methods=['GET', 'POST'])


		db.session.add(user)
		db.session.commit()

		return redirect(url_for('post'))


	return render_template('register.html', title='Register', form=form)


@app.route('/post', methods=['GET', 'POST'])

def outfit():
    form = OutfitForm()
          outfitData = outfits(
            title = form.title.data,
            content = form.content.data,
            author=current_user
        )

        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('home'))

    else:
        print(form.errors)


    return render_template('post.html', title='Post', form=form)




