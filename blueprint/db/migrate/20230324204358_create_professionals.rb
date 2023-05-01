class CreateProfessionals < ActiveRecord::Migration[7.0]
  def change
    create_table :professionals do |t|
      t.string :company
      t.string :slogan
      t.text :about
      t.text :looking
      t.text :benefits
      t.string :address
      t.string :phone
      t.string :email

      t.timestamps
    end
  end
end
