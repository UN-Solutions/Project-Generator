class MluserinputsController < ApplicationController
  before_action :set_mluserinput, only: %i[ show edit update destroy ]

  # GET /mluserinputs or /mluserinputs.json
  def index
    @mluserinputs = Mluserinput.all
  end

  # GET /mluserinputs/1 or /mluserinputs/1.json
  def show
  end

  # GET /mluserinputs/new
  def new
    @mluserinput = Mluserinput.new
  end

  # GET /mluserinputs/1/edit
  def edit
  end

  # POST /mluserinputs or /mluserinputs.json
  def create
    @mluserinput = Mluserinput.new(mluserinput_params)

    respond_to do |format|
      if @mluserinput.save
        format.html { redirect_to mluserinput_url(@mluserinput), notice: "Mluserinput was successfully created." }
        format.json { render :show, status: :created, location: @mluserinput }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @mluserinput.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /mluserinputs/1 or /mluserinputs/1.json
  def update
    respond_to do |format|
      if @mluserinput.update(mluserinput_params)
        format.html { redirect_to mluserinput_url(@mluserinput), notice: "Mluserinput was successfully updated." }
        format.json { render :show, status: :ok, location: @mluserinput }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @mluserinput.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /mluserinputs/1 or /mluserinputs/1.json
  def destroy
    @mluserinput.destroy

    respond_to do |format|
      format.html { redirect_to mluserinputs_url, notice: "Mluserinput was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_mluserinput
      @mluserinput = Mluserinput.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def mluserinput_params
      params.require(:mluserinput).permit(:title, :subject, :subtopics, :mlinput)
    end
end
