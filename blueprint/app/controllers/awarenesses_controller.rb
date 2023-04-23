class AwarenessesController < ApplicationController
  before_action :set_awareness, only: %i[ show edit update destroy ]

  def download_pdf
    send_file "#{Rails.root}/awareness.pdf", type: "application/pdf", x_sendfile: true
  end

  # GET /awarenesses or /awarenesses.json
  def index
    @awarenesses = Awareness.all
    @our_input = Awareness.order("id DESC").first
    @output = `/home/migui/programs/miniconda3/envs/seniorProj/bin/python awareness.py "#{@our_input.inspect}"` # first argument is python Path, if environment change path to environment
  end

  # GET /awarenesses/1 or /awarenesses/1.json
  def show
  end

  # GET /awarenesses/new
  def new
    @awareness = Awareness.new
  end

  # GET /awarenesses/1/edit
  def edit
  end

  # POST /awarenesses or /awarenesses.json
  def create
    @awareness = Awareness.new(awareness_params)

    respond_to do |format|
      if @awareness.save
        format.html { redirect_to awareness_url(@awareness), notice: "Awareness was successfully created." }
        format.json { render :show, status: :created, location: @awareness }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @awareness.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /awarenesses/1 or /awarenesses/1.json
  def update
    respond_to do |format|
      if @awareness.update(awareness_params)
        format.html { redirect_to awareness_url(@awareness), notice: "Awareness was successfully updated." }
        format.json { render :show, status: :ok, location: @awareness }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @awareness.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /awarenesses/1 or /awarenesses/1.json
  def destroy
    @awareness.destroy

    respond_to do |format|
      format.html { redirect_to awarenesses_url, notice: "Awareness was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_awareness
      @awareness = Awareness.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def awareness_params
      params.require(:awareness).permit(:title, :subject, :subtopics)
    end
end
