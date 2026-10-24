html = """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Orejitas y Patitas</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Segoe UI,Arial,sans-serif}
body{background:#F8F9FA;color:#1B263B}.oculto{display:none!important}
#login{min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#2D6A4F,#1B4332)}
.login-card{background:#fff;padding:40px;border-radius:16px;width:380px;text-align:center}
.login-card h1{font-size:28px;color:#2D6A4F;margin-bottom:6px}.login-card p{color:#415A77;margin-bottom:24px}
.login-card input{width:100%;padding:12px;font-size:16px;border:2px solid #E0E1DD;border-radius:8px;text-align:center;margin-bottom:12px}
.btn{background:#2D6A4F;color:#fff;border:none;padding:10px 22px;font-size:14px;font-weight:bold;border-radius:8px;cursor:pointer}
header{background:#fff;border-bottom:2px solid #2D6A4F;padding:12px 24px;display:flex;justify-content:space-between;align-items:center}
header h1{font-size:22px;color:#2D6A4F}.usuario{font-size:14px;color:#415A77}
nav{display:flex;gap:2px;background:#E9ECEF;padding:8px 12px 0;flex-wrap:wrap;border-bottom:2px solid #2D6A4F}
nav button{border:none;padding:12px 16px;font-size:13px;font-weight:bold;color:#415A77;background:transparent;cursor:pointer}
nav button.activa{background:#2D6A4F;color:#fff}
main{padding:24px;max-width:1400px;margin:0 auto}
h2{color:#2D6A4F;margin-bottom:18px;border-bottom:2px solid #2D6A4F;padding-bottom:8px}
.card{background:#fff;border:1px solid #E0E1DD;border-radius:12px;padding:22px;margin-bottom:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
label{font-size:13px;font-weight:bold;color:#415A77;display:block;margin-bottom:4px}
input,select{width:100%;padding:10px;border:1px solid #E0E1DD;border-radius:8px;font-size:14px}
table{width:100%;border-collapse:collapse;margin-top:14px;font-size:14px}
th{background:#D8F3DC;color:#1B4332;text-align:left;padding:10px}
td{padding:10px;border-bottom:1px solid #E0E1DD}
button.eliminar{background:#E63946;color:#fff;border:none;padding:5px 10px;border-radius:6px;cursor:pointer}
.tabs-int{display:flex;gap:4px;margin-bottom:16px;border-bottom:2px solid #E0E1DD;flex-wrap:wrap}
.tabs-int button{border:none;padding:10px 18px;background:transparent;cursor:pointer;font-weight:bold;color:#415A77;border-bottom:3px solid transparent;font-size:13px}
.tabs-int button.activa{color:#2D6A4F;border-bottom-color:#2D6A4F;background:#D8F3DC}
.panel-int{display:none}.panel-int.activa{display:block}
.ok{color:#2D6A4F;font-weight:bold}
.top-row{display:flex;gap:20px;margin-bottom:20px;align-items:flex-start;flex-wrap:wrap}
.inscripcion-box{background:#D8F3DC;padding:16px 20px;border-radius:10px;border-left:5px solid #2D6A4F;min-width:220px;flex:1;max-width:350px}
.inscripcion-box label{font-size:14px;color:#1B4332;font-weight:bold;margin-bottom:6px;display:block}
.inscripcion-box input{font-size:16px;font-weight:bold;padding:10px 12px;background:#fff;border:2px solid #2D6A4F;border-radius:8px;width:100%}
.foto-container{display:flex;flex-direction:column;align-items:center;gap:6px}
.foto-container>label{font-size:14px;font-weight:bold;color:#415A77}
.foto-box{display:inline-flex;align-items:center;justify-content:center;border:3px dashed #2D6A4F;border-radius:12px;overflow:hidden;background:#fff;cursor:pointer;padding:5px}
.foto-box.vacia{width:160px;height:160px}
.foto-box img{max-width:200px;max-height:280px;width:auto;height:auto;display:block;border-radius:8px}
.foto-box span{color:#778DA9;font-size:13px;text-align:center;padding:10px}
@media (max-width:768px){
  .top-row{flex-direction:column}
  .inscripcion-box{max-width:100%}
  main{padding:12px}
  .card{padding:14px}
  nav button{padding:8px 10px;font-size:12px}
  header h1{font-size:18px}
  .grid{grid-template-columns:1fr}
}
</style></head><body>
<div id="login"><div class="login-card">
<h1>Orejitas y Patitas</h1><p>Sistema de Guarderia Canina</p>
<input type="text" id="cc" placeholder="Ingresa tu cedula" maxlength="15">
<br><button class="btn" onclick="ingresar()">Ingresar</button>
<div id="error-login" style="color:#E63946;font-size:14px;margin-top:8px"></div>
</div></div>
<div id="app" class="oculto">
<header><h1>Orejitas y Patitas</h1><div class="usuario"><span id="cc-actual"></span></div></header>
<nav>
<button class="activa" data-tab="guarderia">Guarderia</button>
<button data-tab="cachorros">Cachorros</button>
<button data-tab="conductores">Conductores</button>
<button data-tab="vehiculos">Vehiculos</button>
<button data-tab="planes">Planes</button>
<button data-tab="pagos">Pagos</button>
<button data-tab="resumen">Resumen</button>
</nav>
<main>
<section id="tab-guarderia">
<h2>Configuracion de la Guarderia</h2>
<div class="card">
<div class="grid">
<div><label>Nombre</label><input id="g-nombre"></div>
<div><label>Direccion</label><input id="g-direccion"></div>
<div><label>Telefono</label><input id="g-telefono"></div>
<div><label>Persona de contacto</label><input id="g-contacto"></div>
<div><label>Zona</label><select id="g-zona"></select></div>
<div><label>Horario apertura</label><input id="g-apertura" type="time" value="07:00"></div>
<div><label>Horario cierre</label><input id="g-cierre" type="time" value="19:00"></div>
</div>
<p style="margin-top:18px"><button class="btn" onclick="guardarGuarderia()">Guardar</button> <span class="ok" id="g-msg"></span></p>
</div>
</section>
<section id="tab-cachorros" class="oculto">
<h2>Cachorros</h2>
<div class="tabs-int">
<button class="activa" onclick="mostrarSubTab('datos',this)">Datos</button>
<button onclick="mostrarSubTab('medica',this)">Info Medica</button>
<button onclick="mostrarSubTab('alimentacion',this)">Alimentacion</button>
<button onclick="mostrarSubTab('plan',this)">Plan</button>
<button onclick="mostrarSubTab('asistencia',this)">Asistencia</button>
<button onclick="mostrarSubTab('pagos',this)">Pagos</button>
<button onclick="mostrarSubTab('novedades',this)">Novedades</button>
</div>
<div id="subtab-datos" class="panel-int activa">
<div class="card"><h3>Agregar cachorro</h3>
<div class="top-row">
<div class="inscripcion-box">
<label>Numero de inscripcion</label>
<input id="c-inscripcion" placeholder="Se genera automatico">
</div>
<div class="foto-container">
<label>Foto del cachorro</label>
<div class="foto-box vacia" id="foto-preview" onclick="document.getElementById('c-foto').click()">
<span>📷<br>Clic para subir foto</span>
</div>
<input type="file" id="c-foto" accept="image/*" style="display:none" onchange="cargarFoto(event)">
</div>
</div>
<div class="grid">
<div><label>Nombre</label><input id="c-nombre"></div>
<div><label>Raza</label><input id="c-raza"></div>
<div><label>Edad</label><input id="c-edad"></div>
<div><label>Sexo</label><select id="c-sexo"><option value="">--</option><option>Macho</option><option>Hembra</option></select></div>
<div><label>Peso (kg)</label><input id="c-peso" type="number" step="0.1"></div>
<div><label>Tamano</label><select id="c-tamano"><option value="">--</option><option>Pequeno</option><option>Mediano</option><option>Grande</option><option>Gigante</option></select></div>
</div>
<h3 style="margin-top:20px">Datos del Dueno</h3>
<div class="grid">
<div><label>Nombre Dueno</label><input id="c-dueno"></div>
<div><label>Telefono</label><input id="c-telefono"></div>
<div><label>Direccion</label><input id="c-direccion"></div>
<div><label>Zona</label><select id="c-zona"></select></div>
</div>
<h3 style="margin-top:20px">Plan</h3>
<div class="grid">
<div><label>Plan</label><select id="c-plan"></select></div>
<div><label>Modalidad</label><select id="c-modalidad"><option value="">--</option><option>Diurno</option><option>Nocturno</option><option>Mixto</option></select></div>
</div>
<p style="margin-top:16px"><button class="btn" onclick="agregarCachorro()">Agregar</button></p>
</div>
<div class="card"><h3>Lista (<span id="count-cachorros">0</span>)</h3><div id="tabla-cachorros"></div></div>
</div>
<div id="subtab-medica" class="panel-int"><div class="card"><h3>Info Medica</h3><p style="padding:40px;text-align:center">Paso 2 - En desarrollo</p></div></div>
<div id="subtab-alimentacion" class="panel-int"><div class="card"><h3>Alimentacion</h3><p style="padding:40px;text-align:center">Paso 3 - En desarrollo</p></div></div>
<div id="subtab-plan" class="panel-int"><div class="card"><h3>Plan</h3><p style="padding:40px;text-align:center">Paso 4 - En desarrollo</p></div></div>
<div id="subtab-asistencia" class="panel-int"><div class="card"><h3>Asistencia</h3><p style="padding:40px;text-align:center">Paso 5 - En desarrollo</p></div></div>
<div id="subtab-pagos" class="panel-int"><div class="card"><h3>Pagos</h3><p style="padding:40px;text-align:center">Paso 6 - En desarrollo</p></div></div>
<div id="subtab-novedades" class="panel-int"><div class="card"><h3>Novedades</h3><p style="padding:40px;text-align:center">Paso 7 - En desarrollo</p></div></div>
</section>
<section id="tab-conductores" class="oculto"><h2>Conductores</h2><div class="card"><p>En desarrollo</p></div></section>
<section id="tab-vehiculos" class="oculto"><h2>Vehiculos</h2><div class="card"><p>En desarrollo</p></div></section>
<section id="tab-planes" class="oculto"><h2>Planes</h2><div class="card"><p>En desarrollo</p></div></section>
<section id="tab-pagos" class="oculto"><h2>Pagos</h2><div class="card"><p>En desarrollo</p></div></section>
<section id="tab-resumen" class="oculto"><h2>Resumen</h2><div class="card"><p>En desarrollo</p></div></section>
</main></div>
<script>
const CEDULAS=['19381992','53177327','1020717529'];
const ZONAS=['Chapinero','Usaquen','Suba','Kennedy','Fontibon','Teusaquillo','Barrios Unidos','Engativa','Bosa','San Cristobal','Usme','Tunjuelito','Ciudad Bolivar','Rafael Uribe','Antonio Narino','Santa Fe','Los Martires','Puente Aranda','Cota','Chia'];
let cachorros=[],planes=[],config={guarderia:{}},fotoBase64='';
const val=id=>document.getElementById(id).value.trim();
function mostrarSubTab(id,btn){document.querySelectorAll('.tabs-int button').forEach(b=>b.classList.remove('activa'));btn.classList.add('activa');document.querySelectorAll('.panel-int').forEach(p=>p.classList.remove('activa'));document.getElementById('subtab-'+id).classList.add('activa')}
function cargarFoto(e){const f=e.target.files[0];if(!f)return;if(f.size>500*1024){alert('Foto muy grande (max 500KB)');return}const r=new FileReader();r.onload=ev=>{fotoBase64=ev.target.result;const box=document.getElementById('foto-preview');box.classList.remove('vacia');box.innerHTML='<img src="'+fotoBase64+'">'};r.readAsDataURL(f)}
function calcularSiguienteNumero(){
  if(!cachorros.length)return '001';
  let maxNum=0;
  cachorros.forEach(c=>{
    if(c.inscripcion){
      const n=parseInt(c.inscripcion);
      if(!isNaN(n)&&n>maxNum)maxNum=n;
    }
  });
  return String(maxNum+1).padStart(3,'0');
}
function ingresar(){const cc=val('cc');if(!cc){document.getElementById('error-login').textContent='Escribe tu cedula.';return}if(!CEDULAS.includes(cc)){document.getElementById('error-login').textContent='Cedula no registrada.';return}document.getElementById('login').classList.add('oculto');document.getElementById('app').classList.remove('oculto');document.getElementById('cc-actual').textContent=cc+' (maestro)';cargarZonas('g-zona');cargarZonas('c-zona');cargarPlanes();cargarCachorros();cargarConfig()}
function cargarZonas(id){const z=document.getElementById(id);z.innerHTML='<option value="">-- Selecciona --</option>'+ZONAS.map(x=>'<option>'+x+'</option>').join('')}
function cargarConfig(){fetch('/api/datos').then(r=>r.json()).then(d=>{config=d.config||{guarderia:{}};const g=config.guarderia||{};document.getElementById('g-nombre').value=g.nombre||'';document.getElementById('g-direccion').value=g.direccion||'';document.getElementById('g-telefono').value=g.telefono||'';document.getElementById('g-contacto').value=g.contacto||'';document.getElementById('g-zona').value=g.zona||'';if(g.apertura)document.getElementById('g-apertura').value=g.apertura;if(g.cierre)document.getElementById('g-cierre').value=g.cierre})}
function guardarGuarderia(){config.guarderia={nombre:val('g-nombre'),direccion:val('g-direccion'),telefono:val('g-telefono'),contacto:val('g-contacto'),zona:val('g-zona'),apertura:document.getElementById('g-apertura').value,cierre:document.getElementById('g-cierre').value};fetch('/api/guardar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({clave:'config',datos:config})});document.getElementById('g-msg').textContent='Guardado';setTimeout(()=>document.getElementById('g-msg').textContent='',3000)}
function cargarPlanes(){fetch('/api/datos').then(r=>r.json()).then(d=>{planes=d.planes||[];const p=document.getElementById('c-plan');if(planes.length){p.innerHTML='<option value="">-- Selecciona --</option>'+planes.map(x=>'<option value="'+x.nombre+'">'+x.nombre+' - $'+x.precio+'</option>').join('')}else{p.innerHTML='<option value="">-- Sin planes --</option>'}})}
function cargarCachorros(){fetch('/api/datos').then(r=>r.json()).then(d=>{cachorros=d.cachorros||[];renderCachorros();document.getElementById('c-inscripcion').value=calcularSiguienteNumero()})}
function agregarCachorro(){const c={inscripcion:val('c-inscripcion'),nombre:val('c-nombre'),raza:val('c-raza'),edad:val('c-edad'),sexo:val('c-sexo'),peso:val('c-peso'),tamano:val('c-tamano'),dueno:val('c-dueno'),telefono:val('c-telefono'),direccion:val('c-direccion'),zona:val('c-zona'),plan:val('c-plan'),modalidad:val('c-modalidad'),foto:fotoBase64,vacunas:[],noViajarCon:[]};if(!c.nombre||!c.dueno){alert('Nombre y dueno obligatorios');return}cachorros.push(c);fetch('/api/guardar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({clave:'cachorros',datos:cachorros})});document.getElementById('c-inscripcion').value=calcularSiguienteNumero();document.getElementById('c-nombre').value='';document.getElementById('c-raza').value='';document.getElementById('c-edad').value='';document.getElementById('c-dueno').value='';document.getElementById('c-telefono').value='';document.getElementById('c-direccion').value='';fotoBase64='';const box=document.getElementById('foto-preview');box.classList.add('vacia');box.innerHTML='<span>📷<br>Clic para subir foto</span>';document.getElementById('c-foto').value='';renderCachorros();alert('Cachorro registrado: '+c.nombre+' (Inscripcion: '+c.inscripcion+')')}
function renderCachorros(){document.getElementById('count-cachorros').textContent=cachorros.length;if(!cachorros.length){document.getElementById('tabla-cachorros').innerHTML='<p>Aun no hay cachorros.</p>';return}let html='<table><tr><th>#</th><th>Foto</th><th>Inscripcion</th><th>Nombre</th><th>Raza</th><th>Dueno</th><th>Zona</th><th>Plan</th><th></th></tr>';cachorros.forEach((c,i)=>{html+='<tr><td>'+(i+1)+'</td><td>'+(c.foto?'<img src="'+c.foto+'" style="max-width:60px;max-height:60px;border-radius:6px">':'')+'</td><td><b>'+(c.inscripcion||'--')+'</b></td><td>'+c.nombre+'</td><td>'+(c.raza||'--')+'</td><td>'+c.dueno+'</td><td>'+(c.zona||'--')+'</td><td>'+(c.plan||'--')+'</td><td><button class="eliminar" onclick="eliminarCachorro('+i+')">Eliminar</button></td></tr>'});document.getElementById('tabla-cachorros').innerHTML=html+'</table>'}
function eliminarCachorro(i){if(confirm('Eliminar '+cachorros[i].nombre+'?')){cachorros.splice(i,1);fetch('/api/guardar',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({clave:'cachorros',datos:cachorros})});renderCachorros();document.getElementById('c-inscripcion').value=calcularSiguienteNumero()}}
document.querySelectorAll('nav button').forEach(b=>b.addEventListener('click',function(){document.querySelectorAll('nav button').forEach(x=>x.classList.remove('activa'));this.classList.add('activa');document.querySelectorAll('main section').forEach(s=>s.classList.add('oculto'));document.getElementById('tab-'+this.dataset.tab).classList.remove('oculto')}));
</script></body></html>"""

with open('mi1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('OK: ' + str(len(html)) + ' bytes')