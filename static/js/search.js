const search= document.querySelector("#search");
const tableOutput= document.querySelector("#tableoutput");
const appTable = document.querySelector("#original");
const output = document.querySelector("#output");
tableOutput.style.display="none";
const id = document.querySelector("#ename").value;
search.addEventListener("keyup",(e) =>{
    const searchval = e.target.value;
    if(searchval.length > 0){
        console.log(searchval)
    output.innerHTML='';
    fetch ("/searchstu/"+id,{
        body : JSON.stringify({searchtext: searchval}),
        method : "POST",
    })
    .then((res) => res.json())
    .then((data) =>{
        console.log("data",data);
        appTable.style.display = "none";
        tableOutput.style.display = "block";
        if(data.length === 0){
            tableOutput.innerHTML += `No Results Found`;
            }
        else{
            data.forEach((item)=>{
            output.innerHTML +=` <tr class="table-secondary"><td>${item.name}</td>
            <td>${item.cgpa}</td>
        <td><a href="${item.resume}">Anugrah</a></td>
        <td>${item.mobile}</td>
        <td><input type="checkbox" name='check' value ='${item.id}'></td>
        </tr>`;
            });
            
        }

});   
}
else{
    appTable.style.display = "block";
    tableOutput.style.display = "none";
}
}); 

