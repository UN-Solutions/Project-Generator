class CreatePresentations < ActiveRecord::Migration[7.0]
  def change
    create_table :presentations do |t|
      t.string :title
      t.string :subject
      t.text :subtopics

      t.timestamps
    end
  end
end
