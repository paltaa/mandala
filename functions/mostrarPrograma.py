def mostrarPrograma(programa):
    return(
                 <li>
                   <a href="{{programa.id}}" title="{{programa.title}}">
                        <div class="imgEffect" style="background-image: url('{{programa.img.url}}'  );">
                            </div>
                            <div class="layerLists">
                              <h2>{{programa.title}}</h2>
                            </div>
                            <div class="boxTxt">
                                <p>{{programa.short}} </p>
                            </div>
                        </a>
                    </li>)

                    )
