# We need ruby 3.1.0. I found this from Docker Hub
FROM ruby:3.1.0

EXPOSE 3000

WORKDIR /usr/src/app


# Install the correct bundler version
RUN gem install bundler:2.3.3

# Copy the files required for dependencies to be installed
COPY Gemfile* ./

# Install all dependencies
RUN bundle install


# Copy all of the source code
COPY . .

# We pick the production mode since we have no intention of developing the software inside the container.
# Run database migrations by following instructions from README
RUN rails db:migrate RAILS_ENV=production

# Precompile assets by following instructions from README
RUN rake assets:precompile

# And finally the command to run the application
CMD ["rails", "s", "-e", "production"]


# 1. Created an Account on Render.com
# 2. Create a new Web Service
# 3. Entered the link to my image from Docker Hub: kpetrela83/rails:latest
# 4. Chose the name, region, free plan, then clicked Create Web Service at the bottom of the page.

# 5. Thenthe image was deployed on render.com and when the service was live I pasted the link below to my browser.
https://rails-latest.onrender.com/




