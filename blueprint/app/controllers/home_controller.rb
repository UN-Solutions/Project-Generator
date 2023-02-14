class HomeController < ApplicationController
  def home

    our_input = "heart"
    @heart = `python3 test.py "#{our_input}"`

  end
end
