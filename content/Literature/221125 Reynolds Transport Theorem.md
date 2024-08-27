Status: #finished 
## Theorem
In real world situation it is easier to easier to analyse a control volume (control volume analysis) rather than keep track of an entire system (control system analysis). This means that we have to meaningfully convert the [[220430 Material Derivative or Substantial Derivative or Lagrangian Derivative|Lagrangian Derivatives]] to Eulerian Derivatives. 

Say we have a Property $B$. The amount of $B$ in a control volume can be evaluated as follows

$$
B_{\text{CV}}=\int_{\text{CV}} \beta\ dm =\int_{\text{CV}} \beta\rho \ dV
$$

Where $\beta \rightarrow \frac{dB}{dm}$ 
The **Reynolds Transport theorem** states that: 

$$
\begin{align}
\text{Rate of Change of } B\text{ in the Sys} &= \text{(Accumulation rate of }\beta\text{ inside CV) + (Net Outflux of }\beta\text{ through CS)}\\
\text{Rate of Change of } B\text{ in the Sys} &=\text{(Accumulation rate of }\beta\text{ inside CV )+ }(\beta\text{ Outflow from CV } - \beta\text{ Inflow to CV)}
\end{align}
$$


$$
\frac{d}{dt}
(B_\text{sys})=\frac{d}{dt}\left(\int_{\text{cv}}\beta \rho \ dV \right)+\int_{\text{CS}}\beta \rho v \cos\theta  \ dA_{out}-\int_{\text{CS}}\beta \rho v \cos \theta \ dA_{in}
$$

Considering the Surface normal vector $\vec n$, above equation can be simplified to

$$
\boxed{
\frac{d}{dt}
(B_\text{sys})=
\frac{d}{dt}\left(\int_{\text{CV}}\beta \rho \ dV \right)+ 
\int_{\text{CS}}\beta \rho (\vec v\cdot \vec n)  \ dA
}
$$

### Special Cases
- **Steady Flow:**
	
$$
\frac{d}{dt}(B_\text{sys})= \int_{\text{CS}}\beta\rho(\vec v \cdot \vec n)dA
$$

- **Relative Velocity**
Where $\vec v_r = \vec v - \vec v_s$ 

$$
\frac{d}{dt}
(B_\text{sys})=
\frac{d}{dt}\left(\int_{\text{cv}}\beta \rho \ dV \right)+ 
\int_{\text{CS}}\beta \rho (\vec v_r\cdot \vec n)  \ dA
$$



