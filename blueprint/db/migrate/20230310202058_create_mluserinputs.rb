class CreateMluserinputs < ActiveRecord::Migration[7.0]
  def change
    create_table :mluserinputs do |t|
      t.string :title
      t.string :subject
      t.text :subtopics
      t.text :mlinput

      t.timestamps
    end
  end
end
