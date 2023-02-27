Rails.application.routes.draw do

  resources :userinputs
  get 'download_pdf', to: "userinputs#download_pdf"
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
