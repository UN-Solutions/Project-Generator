Rails.application.routes.draw do
  resources :presentations
  resources :professionals
  resources :awarenesses
  root 'home#home'
  get 'aboutus', to: 'aboutus#index'
  get 'howto', to: 'howto#index'
  get 'menu', to: 'menu#index'
  resources :userinputs
  get 'download_pdf', to: "userinputs#download_pdf"
  get 'download_apdf', to: "awarenesses#download_pdf"
  get 'download_ppdf', to: "professionals#download_pdf"
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
