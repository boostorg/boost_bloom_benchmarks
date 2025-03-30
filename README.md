# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.45</td>
    <td align="right">4.68</td>
    <td align="right">3.73</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.17</td>
    <td align="right">10.66</td>
    <td align="right">16.53</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.01</td>
    <td align="right">4.35</td>
    <td align="right">4.35</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.87</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.95</td>
    <td align="right">15.54</td>
    <td align="right">17.62</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.79</td>
    <td align="right">4.93</td>
    <td align="right">4.95</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.23</td>
    <td align="right">18.84</td>
    <td align="right">16.53</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.38</td>
    <td align="right">5.31</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.23</td>
    <td align="right">6.26</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.90</td>
    <td align="right">23.13</td>
    <td align="right">16.81</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.41</td>
    <td align="right">6.06</td>
    <td align="right">5.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.71</td>
    <td align="right">6.59</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.08</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.54</td>
    <td align="right">6.73</td>
    <td align="right">6.88</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.96</td>
    <td align="right">3.27</td>
    <td align="right">3.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.08</td>
    <td align="right">8.87</td>
    <td align="right">8.88</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.18</td>
    <td align="right">10.06</td>
    <td align="right">10.07</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.19</td>
    <td align="right">13.70</td>
    <td align="right">13.75</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.88</td>
    <td align="right">14.16</td>
    <td align="right">14.23</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.75</td>
    <td align="right">5.79</td>
    <td align="right">3.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.03</td>
    <td align="right">15.44</td>
    <td align="right">15.47</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.06</td>
    <td align="right">17.50</td>
    <td align="right">17.53</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.87</td>
    <td align="right">5.87</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.98</td>
    <td align="right">3.26</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.40</td>
    <td align="right">5.09</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.53</td>
    <td align="right">5.03</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.04</td>
    <td align="right">3.32</td>
    <td align="right">3.34</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.24</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.46</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.49</td>
    <td align="right">5.56</td>
    <td align="right">3.86</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.06</td>
    <td align="right">7.71</td>
    <td align="right">5.94</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.89</td>
    <td align="right">7.53</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.50</td>
    <td align="right">5.59</td>
    <td align="right">3.80</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.14</td>
    <td align="right">9.14</td>
    <td align="right">6.04</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.32</td>
    <td align="right">9.06</td>
    <td align="right">5.93</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.99</td>
    <td align="right">18.54</td>
    <td align="right">6.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.21</td>
    <td align="right">11.06</td>
    <td align="right">16.94</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.44</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.23</td>
    <td align="right">5.37</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.09</td>
    <td align="right">17.08</td>
    <td align="right">17.86</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.02</td>
    <td align="right">5.07</td>
    <td align="right">5.15</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.87</td>
    <td align="right">6.34</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">28.67</td>
    <td align="right">29.43</td>
    <td align="right">17.81</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.30</td>
    <td align="right">6.48</td>
    <td align="right">6.31</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.43</td>
    <td align="right">7.29</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">46.54</td>
    <td align="right">39.91</td>
    <td align="right">19.26</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.08</td>
    <td align="right">10.49</td>
    <td align="right">9.53</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.68</td>
    <td align="right">9.08</td>
    <td align="right">9.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.68</td>
    <td align="right">6.49</td>
    <td align="right">6.50</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.06</td>
    <td align="right">7.47</td>
    <td align="right">7.71</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.37</td>
    <td align="right">3.80</td>
    <td align="right">3.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.39</td>
    <td align="right">9.45</td>
    <td align="right">9.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.20</td>
    <td align="right">10.08</td>
    <td align="right">10.12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.72</td>
    <td align="right">3.38</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.28</td>
    <td align="right">15.08</td>
    <td align="right">15.13</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.90</td>
    <td align="right">15.65</td>
    <td align="right">15.55</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.76</td>
    <td align="right">6.87</td>
    <td align="right">4.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.39</td>
    <td align="right">20.03</td>
    <td align="right">18.67</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.41</td>
    <td align="right">22.94</td>
    <td align="right">22.46</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.38</td>
    <td align="right">9.60</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.36</td>
    <td align="right">3.73</td>
    <td align="right">3.70</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.92</td>
    <td align="right">5.65</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.03</td>
    <td align="right">5.49</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.35</td>
    <td align="right">3.69</td>
    <td align="right">3.67</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.46</td>
    <td align="right">4.77</td>
    <td align="right">4.76</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.81</td>
    <td align="right">5.52</td>
    <td align="right">5.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.69</td>
    <td align="right">7.18</td>
    <td align="right">5.10</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.63</td>
    <td align="right">9.82</td>
    <td align="right">7.79</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.80</td>
    <td align="right">9.55</td>
    <td align="right">7.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.08</td>
    <td align="right">9.05</td>
    <td align="right">7.13</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">11.60</td>
    <td align="right">13.64</td>
    <td align="right">9.10</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.29</td>
    <td align="right">15.12</td>
    <td align="right">16.84</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.46</td>
    <td align="right">4.21</td>
    <td align="right">3.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.27</td>
    <td align="right">9.01</td>
    <td align="right">15.62</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.33</td>
    <td align="right">4.07</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.88</td>
    <td align="right">4.56</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.89</td>
    <td align="right">13.63</td>
    <td align="right">16.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.84</td>
    <td align="right">4.73</td>
    <td align="right">4.57</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.48</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.29</td>
    <td align="right">16.60</td>
    <td align="right">15.92</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.35</td>
    <td align="right">5.26</td>
    <td align="right">5.09</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.91</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.13</td>
    <td align="right">22.66</td>
    <td align="right">15.89</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.82</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.95</td>
    <td align="right">3.28</td>
    <td align="right">3.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.04</td>
    <td align="right">3.59</td>
    <td align="right">3.59</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.16</td>
    <td align="right">3.48</td>
    <td align="right">3.52</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.59</td>
    <td align="right">2.51</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.72</td>
    <td align="right">3.36</td>
    <td align="right">3.37</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.14</td>
    <td align="right">2.27</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.65</td>
    <td align="right">6.23</td>
    <td align="right">6.43</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.89</td>
    <td align="right">6.19</td>
    <td align="right">6.12</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.21</td>
    <td align="right">4.40</td>
    <td align="right">3.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.03</td>
    <td align="right">6.67</td>
    <td align="right">6.69</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.31</td>
    <td align="right">7.31</td>
    <td align="right">7.08</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.22</td>
    <td align="right">4.38</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.59</td>
    <td align="right">2.35</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.58</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.70</td>
    <td align="right">3.94</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.70</td>
    <td align="right">2.40</td>
    <td align="right">2.39</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.90</td>
    <td align="right">3.73</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.90</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.24</td>
    <td align="right">4.32</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.54</td>
    <td align="right">6.12</td>
    <td align="right">4.59</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.68</td>
    <td align="right">5.97</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.28</td>
    <td align="right">4.33</td>
    <td align="right">2.97</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.74</td>
    <td align="right">7.15</td>
    <td align="right">4.94</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.81</td>
    <td align="right">7.02</td>
    <td align="right">4.67</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.58</td>
    <td align="right">16.87</td>
    <td align="right">6.60</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.84</td>
    <td align="right">10.51</td>
    <td align="right">16.47</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.83</td>
    <td align="right">4.63</td>
    <td align="right">4.49</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.49</td>
    <td align="right">5.19</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.69</td>
    <td align="right">15.37</td>
    <td align="right">16.96</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.29</td>
    <td align="right">5.10</td>
    <td align="right">4.96</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.98</td>
    <td align="right">5.78</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">23.83</td>
    <td align="right">24.82</td>
    <td align="right">16.99</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.46</td>
    <td align="right">6.31</td>
    <td align="right">6.13</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.17</td>
    <td align="right">7.83</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">42.24</td>
    <td align="right">39.92</td>
    <td align="right">20.02</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.79</td>
    <td align="right">9.61</td>
    <td align="right">15.23</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">5.61</td>
    <td align="right">6.20</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.53</td>
    <td align="right">4.13</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.57</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.03</td>
    <td align="right">3.02</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.03</td>
    <td align="right">3.69</td>
    <td align="right">3.66</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.05</td>
    <td align="right">4.18</td>
    <td align="right">4.22</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.47</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.07</td>
    <td align="right">7.79</td>
    <td align="right">7.99</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.26</td>
    <td align="right">8.07</td>
    <td align="right">8.04</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.45</td>
    <td align="right">5.85</td>
    <td align="right">4.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">9.10</td>
    <td align="right">10.99</td>
    <td align="right">10.58</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">9.62</td>
    <td align="right">11.68</td>
    <td align="right">12.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.77</td>
    <td align="right">8.39</td>
    <td align="right">7.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.07</td>
    <td align="right">2.92</td>
    <td align="right">2.95</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.18</td>
    <td align="right">4.73</td>
    <td align="right">4.71</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.27</td>
    <td align="right">4.60</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.96</td>
    <td align="right">2.79</td>
    <td align="right">2.78</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.20</td>
    <td align="right">4.05</td>
    <td align="right">4.13</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.33</td>
    <td align="right">4.53</td>
    <td align="right">4.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.54</td>
    <td align="right">5.62</td>
    <td align="right">3.92</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.62</td>
    <td align="right">7.53</td>
    <td align="right">5.91</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.03</td>
    <td align="right">7.61</td>
    <td align="right">6.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.88</td>
    <td align="right">9.24</td>
    <td align="right">6.20</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.04</td>
    <td align="right">11.53</td>
    <td align="right">8.07</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.14</td>
    <td align="right">11.20</td>
    <td align="right">7.99</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">19.76</td>
    <td align="right">4.32</td>
    <td align="right">3.02</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.35</td>
    <td align="right">4.38</td>
    <td align="right">11.90</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.39</td>
    <td align="right">1.26</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.74</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.44</td>
    <td align="right">7.49</td>
    <td align="right">12.88</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.41</td>
    <td align="right">1.49</td>
    <td align="right">1.49</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.80</td>
    <td align="right">1.57</td>
    <td align="right">1.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.72</td>
    <td align="right">9.32</td>
    <td align="right">12.07</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.64</td>
    <td align="right">1.66</td>
    <td align="right">1.67</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.82</td>
    <td align="right">1.80</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.54</td>
    <td align="right">10.68</td>
    <td align="right">11.22</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.16</td>
    <td align="right">2.08</td>
    <td align="right">2.00</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.93</td>
    <td align="right">1.66</td>
    <td align="right">1.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.49</td>
    <td align="right">3.62</td>
    <td align="right">1.85</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.40</td>
    <td align="right">1.89</td>
    <td align="right">1.93</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.14</td>
    <td align="right">1.89</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.20</td>
    <td align="right">2.88</td>
    <td align="right">2.23</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.02</td>
    <td align="right">2.39</td>
    <td align="right">2.29</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.70</td>
    <td align="right">1.51</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.17</td>
    <td align="right">3.13</td>
    <td align="right">3.14</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.38</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.21</td>
    <td align="right">2.70</td>
    <td align="right">1.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.15</td>
    <td align="right">4.23</td>
    <td align="right">4.13</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.22</td>
    <td align="right">4.20</td>
    <td align="right">4.21</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.19</td>
    <td align="right">3.17</td>
    <td align="right">1.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.13</td>
    <td align="right">1.85</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.48</td>
    <td align="right">1.84</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">1.89</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.36</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.46</td>
    <td align="right">2.08</td>
    <td align="right">2.08</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.98</td>
    <td align="right">2.35</td>
    <td align="right">2.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.16</td>
    <td align="right">2.45</td>
    <td align="right">1.92</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.41</td>
    <td align="right">2.93</td>
    <td align="right">3.06</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.69</td>
    <td align="right">3.10</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.94</td>
    <td align="right">2.85</td>
    <td align="right">1.75</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.98</td>
    <td align="right">3.76</td>
    <td align="right">4.11</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.92</td>
    <td align="right">3.81</td>
    <td align="right">3.78</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">28.50</td>
    <td align="right">13.79</td>
    <td align="right">8.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.56</td>
    <td align="right">7.92</td>
    <td align="right">17.75</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">1.95</td>
    <td align="right">3.56</td>
    <td align="right">3.32</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.78</td>
    <td align="right">2.83</td>
    <td align="right">2.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.43</td>
    <td align="right">21.49</td>
    <td align="right">22.68</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.86</td>
    <td align="right">6.51</td>
    <td align="right">4.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.33</td>
    <td align="right">5.76</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">40.51</td>
    <td align="right">32.73</td>
    <td align="right">22.26</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">8.98</td>
    <td align="right">8.13</td>
    <td align="right">7.84</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.18</td>
    <td align="right">9.25</td>
    <td align="right">8.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">67.35</td>
    <td align="right">50.68</td>
    <td align="right">24.76</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.51</td>
    <td align="right">10.22</td>
    <td align="right">9.37</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.18</td>
    <td align="right">7.94</td>
    <td align="right">7.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.04</td>
    <td align="right">2.81</td>
    <td align="right">3.48</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.48</td>
    <td align="right">3.91</td>
    <td align="right">3.67</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.06</td>
    <td align="right">3.46</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.57</td>
    <td align="right">7.39</td>
    <td align="right">7.99</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.95</td>
    <td align="right">8.08</td>
    <td align="right">9.22</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.73</td>
    <td align="right">6.67</td>
    <td align="right">6.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.16</td>
    <td align="right">9.92</td>
    <td align="right">11.60</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">15.35</td>
    <td align="right">12.67</td>
    <td align="right">11.48</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.85</td>
    <td align="right">10.72</td>
    <td align="right">7.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">17.77</td>
    <td align="right">17.05</td>
    <td align="right">18.43</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.02</td>
    <td align="right">17.36</td>
    <td align="right">17.71</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.06</td>
    <td align="right">13.68</td>
    <td align="right">8.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.24</td>
    <td align="right">4.32</td>
    <td align="right">3.19</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.67</td>
    <td align="right">4.58</td>
    <td align="right">4.33</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.24</td>
    <td align="right">4.29</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.93</td>
    <td align="right">5.95</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.68</td>
    <td align="right">8.47</td>
    <td align="right">9.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.12</td>
    <td align="right">4.68</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.36</td>
    <td align="right">7.47</td>
    <td align="right">5.01</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.48</td>
    <td align="right">8.73</td>
    <td align="right">8.70</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.46</td>
    <td align="right">8.53</td>
    <td align="right">8.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.46</td>
    <td align="right">10.42</td>
    <td align="right">5.96</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.29</td>
    <td align="right">13.25</td>
    <td align="right">13.52</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.82</td>
    <td align="right">13.63</td>
    <td align="right">13.47</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.61</td>
    <td align="right">5.68</td>
    <td align="right">3.88</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.23</td>
    <td align="right">12.43</td>
    <td align="right">16.99</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.85</td>
    <td align="right">4.30</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.01</td>
    <td align="right">5.36</td>
    <td align="right">5.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.77</td>
    <td align="right">17.78</td>
    <td align="right">17.61</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.77</td>
    <td align="right">4.78</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.00</td>
    <td align="right">5.92</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.64</td>
    <td align="right">21.33</td>
    <td align="right">16.73</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.59</td>
    <td align="right">5.34</td>
    <td align="right">5.41</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.37</td>
    <td align="right">6.56</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.12</td>
    <td align="right">27.63</td>
    <td align="right">17.32</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.90</td>
    <td align="right">5.91</td>
    <td align="right">5.96</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.45</td>
    <td align="right">7.45</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">8.01</td>
    <td align="right">5.62</td>
    <td align="right">5.60</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.24</td>
    <td align="right">5.66</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.41</td>
    <td align="right">3.98</td>
    <td align="right">3.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.12</td>
    <td align="right">8.54</td>
    <td align="right">8.58</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.33</td>
    <td align="right">8.07</td>
    <td align="right">7.95</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.87</td>
    <td align="right">4.91</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.45</td>
    <td align="right">11.20</td>
    <td align="right">11.05</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.96</td>
    <td align="right">10.70</td>
    <td align="right">10.77</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.09</td>
    <td align="right">7.12</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.77</td>
    <td align="right">14.11</td>
    <td align="right">14.29</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.38</td>
    <td align="right">13.57</td>
    <td align="right">13.64</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.08</td>
    <td align="right">7.11</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.27</td>
    <td align="right">3.88</td>
    <td align="right">3.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.51</td>
    <td align="right">5.47</td>
    <td align="right">5.55</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.74</td>
    <td align="right">5.53</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.29</td>
    <td align="right">5.58</td>
    <td align="right">4.75</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.73</td>
    <td align="right">5.81</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.96</td>
    <td align="right">7.08</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.10</td>
    <td align="right">6.97</td>
    <td align="right">5.06</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">10.04</td>
    <td align="right">9.46</td>
    <td align="right">7.55</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.59</td>
    <td align="right">9.31</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.18</td>
    <td align="right">6.94</td>
    <td align="right">5.07</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.38</td>
    <td align="right">10.62</td>
    <td align="right">7.58</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.24</td>
    <td align="right">10.29</td>
    <td align="right">7.40</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">46.11</td>
    <td align="right">23.31</td>
    <td align="right">9.69</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.84</td>
    <td align="right">13.05</td>
    <td align="right">17.91</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.06</td>
    <td align="right">4.49</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.11</td>
    <td align="right">5.74</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.18</td>
    <td align="right">20.59</td>
    <td align="right">18.58</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.13</td>
    <td align="right">5.44</td>
    <td align="right">5.50</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.50</td>
    <td align="right">7.77</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">36.55</td>
    <td align="right">39.31</td>
    <td align="right">19.46</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.40</td>
    <td align="right">7.31</td>
    <td align="right">7.28</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.04</td>
    <td align="right">8.91</td>
    <td align="right">14.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">83.30</td>
    <td align="right">83.93</td>
    <td align="right">24.98</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.31</td>
    <td align="right">12.64</td>
    <td align="right">15.82</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.81</td>
    <td align="right">15.83</td>
    <td align="right">15.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.50</td>
    <td align="right">6.31</td>
    <td align="right">6.39</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.61</td>
    <td align="right">6.45</td>
    <td align="right">6.43</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.78</td>
    <td align="right">4.27</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.75</td>
    <td align="right">10.51</td>
    <td align="right">11.30</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">20.97</td>
    <td align="right">9.03</td>
    <td align="right">9.37</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.52</td>
    <td align="right">6.14</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.58</td>
    <td align="right">20.31</td>
    <td align="right">18.44</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.35</td>
    <td align="right">15.24</td>
    <td align="right">19.41</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">10.92</td>
    <td align="right">14.32</td>
    <td align="right">12.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">34.78</td>
    <td align="right">30.36</td>
    <td align="right">33.15</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">38.87</td>
    <td align="right">28.78</td>
    <td align="right">25.22</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">14.16</td>
    <td align="right">19.46</td>
    <td align="right">13.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.67</td>
    <td align="right">4.18</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.06</td>
    <td align="right">6.17</td>
    <td align="right">5.96</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.12</td>
    <td align="right">5.82</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.86</td>
    <td align="right">6.11</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.78</td>
    <td align="right">8.72</td>
    <td align="right">7.16</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.77</td>
    <td align="right">7.71</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.94</td>
    <td align="right">8.87</td>
    <td align="right">8.60</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.55</td>
    <td align="right">11.10</td>
    <td align="right">9.40</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">12.32</td>
    <td align="right">15.23</td>
    <td align="right">15.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.22</td>
    <td align="right">16.96</td>
    <td align="right">14.46</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">18.56</td>
    <td align="right">24.02</td>
    <td align="right">18.81</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">23.05</td>
    <td align="right">21.37</td>
    <td align="right">14.28</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.39</td>
    <td align="right">29.87</td>
    <td align="right">13.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.34</td>
    <td align="right">41.68</td>
    <td align="right">36.29</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.46</td>
    <td align="right">15.91</td>
    <td align="right">15.91</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.05</td>
    <td align="right">19.66</td>
    <td align="right">19.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.64</td>
    <td align="right">63.02</td>
    <td align="right">39.31</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.27</td>
    <td align="right">19.33</td>
    <td align="right">19.19</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.04</td>
    <td align="right">18.59</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.37</td>
    <td align="right">78.01</td>
    <td align="right">38.42</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.23</td>
    <td align="right">18.39</td>
    <td align="right">18.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.13</td>
    <td align="right">18.29</td>
    <td align="right">18.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.23</td>
    <td align="right">97.26</td>
    <td align="right">37.66</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.23</td>
    <td align="right">18.75</td>
    <td align="right">18.75</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.99</td>
    <td align="right">20.01</td>
    <td align="right">20.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.20</td>
    <td align="right">20.49</td>
    <td align="right">20.45</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.66</td>
    <td align="right">22.19</td>
    <td align="right">22.16</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.74</td>
    <td align="right">13.77</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.31</td>
    <td align="right">26.75</td>
    <td align="right">26.75</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.70</td>
    <td align="right">29.00</td>
    <td align="right">29.01</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.83</td>
    <td align="right">15.93</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.28</td>
    <td align="right">33.18</td>
    <td align="right">33.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.56</td>
    <td align="right">45.78</td>
    <td align="right">45.79</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.47</td>
    <td align="right">19.54</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.64</td>
    <td align="right">36.19</td>
    <td align="right">36.29</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.64</td>
    <td align="right">55.49</td>
    <td align="right">55.45</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.70</td>
    <td align="right">24.87</td>
    <td align="right">24.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.62</td>
    <td align="right">16.09</td>
    <td align="right">15.73</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.20</td>
    <td align="right">20.52</td>
    <td align="right">20.50</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.62</td>
    <td align="right">22.21</td>
    <td align="right">22.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.10</td>
    <td align="right">20.23</td>
    <td align="right">20.24</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.35</td>
    <td align="right">26.79</td>
    <td align="right">26.81</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.74</td>
    <td align="right">29.08</td>
    <td align="right">29.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.81</td>
    <td align="right">24.99</td>
    <td align="right">25.02</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.30</td>
    <td align="right">33.24</td>
    <td align="right">33.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.48</td>
    <td align="right">45.76</td>
    <td align="right">45.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">34.25</td>
    <td align="right">35.23</td>
    <td align="right">35.26</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.62</td>
    <td align="right">36.12</td>
    <td align="right">36.24</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.55</td>
    <td align="right">55.50</td>
    <td align="right">55.46</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.82</td>
    <td align="right">106.48</td>
    <td align="right">18.70</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.63</td>
    <td align="right">42.72</td>
    <td align="right">39.43</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.82</td>
    <td align="right">16.23</td>
    <td align="right">16.45</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.37</td>
    <td align="right">19.97</td>
    <td align="right">20.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.45</td>
    <td align="right">64.72</td>
    <td align="right">41.97</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">18.35</td>
    <td align="right">32.36</td>
    <td align="right">30.92</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">18.38</td>
    <td align="right">23.37</td>
    <td align="right">19.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">47.68</td>
    <td align="right">79.11</td>
    <td align="right">41.24</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">20.25</td>
    <td align="right">22.58</td>
    <td align="right">22.23</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">20.41</td>
    <td align="right">21.59</td>
    <td align="right">30.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">150.48</td>
    <td align="right">244.20</td>
    <td align="right">80.98</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">43.01</td>
    <td align="right">43.24</td>
    <td align="right">49.31</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">54.14</td>
    <td align="right">51.30</td>
    <td align="right">52.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.86</td>
    <td align="right">22.00</td>
    <td align="right">21.62</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">36.18</td>
    <td align="right">25.42</td>
    <td align="right">24.57</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.10</td>
    <td align="right">14.77</td>
    <td align="right">14.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.45</td>
    <td align="right">41.36</td>
    <td align="right">36.60</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">59.20</td>
    <td align="right">41.89</td>
    <td align="right">53.83</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">15.80</td>
    <td align="right">20.96</td>
    <td align="right">20.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">60.85</td>
    <td align="right">58.22</td>
    <td align="right">41.10</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">71.49</td>
    <td align="right">51.45</td>
    <td align="right">53.92</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">16.97</td>
    <td align="right">25.03</td>
    <td align="right">21.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">46.60</td>
    <td align="right">52.51</td>
    <td align="right">55.87</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">102.73</td>
    <td align="right">90.36</td>
    <td align="right">96.33</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">55.71</td>
    <td align="right">56.70</td>
    <td align="right">55.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.57</td>
    <td align="right">16.83</td>
    <td align="right">16.22</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.19</td>
    <td align="right">22.26</td>
    <td align="right">21.09</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">37.15</td>
    <td align="right">25.04</td>
    <td align="right">23.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">23.18</td>
    <td align="right">27.68</td>
    <td align="right">23.57</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.06</td>
    <td align="right">34.61</td>
    <td align="right">39.44</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">87.91</td>
    <td align="right">51.45</td>
    <td align="right">52.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">84.48</td>
    <td align="right">48.90</td>
    <td align="right">44.01</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">52.51</td>
    <td align="right">49.80</td>
    <td align="right">49.90</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">74.83</td>
    <td align="right">55.10</td>
    <td align="right">58.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">75.14</td>
    <td align="right">90.22</td>
    <td align="right">90.11</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">59.57</td>
    <td align="right">71.47</td>
    <td align="right">67.87</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">98.79</td>
    <td align="right">83.85</td>
    <td align="right">77.86</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.47</td>
    <td align="right">10.16</td>
    <td align="right">6.87</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">14.05</td>
    <td align="right">22.95</td>
    <td align="right">26.71</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.47</td>
    <td align="right">12.30</td>
    <td align="right">12.31</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.69</td>
    <td align="right">13.95</td>
    <td align="right">13.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.68</td>
    <td align="right">35.24</td>
    <td align="right">28.87</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.08</td>
    <td align="right">14.23</td>
    <td align="right">14.07</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.49</td>
    <td align="right">15.36</td>
    <td align="right">15.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.30</td>
    <td align="right">47.74</td>
    <td align="right">30.22</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.77</td>
    <td align="right">15.45</td>
    <td align="right">15.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.58</td>
    <td align="right">16.70</td>
    <td align="right">16.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.49</td>
    <td align="right">60.74</td>
    <td align="right">30.99</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.57</td>
    <td align="right">16.32</td>
    <td align="right">16.29</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.88</td>
    <td align="right">17.81</td>
    <td align="right">17.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.60</td>
    <td align="right">16.20</td>
    <td align="right">16.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.19</td>
    <td align="right">16.66</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.19</td>
    <td align="right">9.44</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.32</td>
    <td align="right">22.90</td>
    <td align="right">22.52</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.35</td>
    <td align="right">22.30</td>
    <td align="right">22.32</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">10.98</td>
    <td align="right">13.96</td>
    <td align="right">14.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.99</td>
    <td align="right">32.13</td>
    <td align="right">32.10</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.53</td>
    <td align="right">30.59</td>
    <td align="right">30.51</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">12.67</td>
    <td align="right">17.54</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.79</td>
    <td align="right">35.71</td>
    <td align="right">35.66</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.00</td>
    <td align="right">35.77</td>
    <td align="right">35.73</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.37</td>
    <td align="right">20.45</td>
    <td align="right">20.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.56</td>
    <td align="right">9.36</td>
    <td align="right">9.40</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.62</td>
    <td align="right">16.14</td>
    <td align="right">16.13</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.19</td>
    <td align="right">16.69</td>
    <td align="right">16.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">12.38</td>
    <td align="right">13.65</td>
    <td align="right">13.72</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.36</td>
    <td align="right">22.48</td>
    <td align="right">22.47</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.21</td>
    <td align="right">22.30</td>
    <td align="right">22.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.07</td>
    <td align="right">17.61</td>
    <td align="right">17.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.93</td>
    <td align="right">32.14</td>
    <td align="right">32.10</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.54</td>
    <td align="right">30.55</td>
    <td align="right">30.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.01</td>
    <td align="right">21.01</td>
    <td align="right">20.93</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.89</td>
    <td align="right">35.70</td>
    <td align="right">35.74</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.02</td>
    <td align="right">35.73</td>
    <td align="right">35.76</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">81.70</td>
    <td align="right">46.58</td>
    <td align="right">11.35</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.43</td>
    <td align="right">23.24</td>
    <td align="right">28.29</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.66</td>
    <td align="right">12.58</td>
    <td align="right">12.86</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">13.05</td>
    <td align="right">14.65</td>
    <td align="right">14.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">20.77</td>
    <td align="right">36.76</td>
    <td align="right">30.42</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">12.85</td>
    <td align="right">14.97</td>
    <td align="right">14.49</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.82</td>
    <td align="right">18.54</td>
    <td align="right">15.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">25.61</td>
    <td align="right">50.22</td>
    <td align="right">37.84</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">26.17</td>
    <td align="right">34.22</td>
    <td align="right">31.58</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">30.07</td>
    <td align="right">33.84</td>
    <td align="right">32.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">92.90</td>
    <td align="right">137.34</td>
    <td align="right">33.53</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">20.24</td>
    <td align="right">19.16</td>
    <td align="right">29.40</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">26.50</td>
    <td align="right">37.36</td>
    <td align="right">46.77</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.26</td>
    <td align="right">17.35</td>
    <td align="right">16.71</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">14.02</td>
    <td align="right">20.00</td>
    <td align="right">20.69</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.50</td>
    <td align="right">9.90</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.92</td>
    <td align="right">29.53</td>
    <td align="right">24.81</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">27.92</td>
    <td align="right">33.97</td>
    <td align="right">26.86</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">10.14</td>
    <td align="right">14.31</td>
    <td align="right">16.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">47.64</td>
    <td align="right">47.47</td>
    <td align="right">40.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">33.45</td>
    <td align="right">43.09</td>
    <td align="right">40.68</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">17.99</td>
    <td align="right">29.05</td>
    <td align="right">20.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">53.77</td>
    <td align="right">60.61</td>
    <td align="right">61.38</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">76.12</td>
    <td align="right">64.65</td>
    <td align="right">62.99</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">33.03</td>
    <td align="right">34.94</td>
    <td align="right">39.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.71</td>
    <td align="right">9.57</td>
    <td align="right">9.51</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.63</td>
    <td align="right">16.72</td>
    <td align="right">16.73</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.34</td>
    <td align="right">17.49</td>
    <td align="right">17.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.79</td>
    <td align="right">13.62</td>
    <td align="right">14.44</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.36</td>
    <td align="right">23.99</td>
    <td align="right">23.19</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.54</td>
    <td align="right">23.46</td>
    <td align="right">23.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">14.27</td>
    <td align="right">21.80</td>
    <td align="right">26.74</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">47.90</td>
    <td align="right">76.52</td>
    <td align="right">67.15</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">41.49</td>
    <td align="right">71.83</td>
    <td align="right">68.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">47.06</td>
    <td align="right">40.61</td>
    <td align="right">37.34</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.78</td>
    <td align="right">65.31</td>
    <td align="right">62.56</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">63.00</td>
    <td align="right">65.54</td>
    <td align="right">74.15</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.15</td>
    <td align="right">8.80</td>
    <td align="right">6.69</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.86</td>
    <td align="right">54.86</td>
    <td align="right">41.56</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">22.14</td>
    <td align="right">20.45</td>
    <td align="right">24.74</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">27.08</td>
    <td align="right">26.82</td>
    <td align="right">29.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.90</td>
    <td align="right">86.27</td>
    <td align="right">46.43</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">24.28</td>
    <td align="right">21.92</td>
    <td align="right">24.31</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.32</td>
    <td align="right">29.55</td>
    <td align="right">30.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">111.30</td>
    <td align="right">98.48</td>
    <td align="right">43.24</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.24</td>
    <td align="right">22.89</td>
    <td align="right">24.52</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.96</td>
    <td align="right">32.05</td>
    <td align="right">31.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.87</td>
    <td align="right">127.73</td>
    <td align="right">46.58</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">28.18</td>
    <td align="right">24.55</td>
    <td align="right">25.19</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.23</td>
    <td align="right">33.59</td>
    <td align="right">34.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.72</td>
    <td align="right">45.59</td>
    <td align="right">46.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.45</td>
    <td align="right">45.60</td>
    <td align="right">46.24</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.62</td>
    <td align="right">24.84</td>
    <td align="right">25.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.35</td>
    <td align="right">60.94</td>
    <td align="right">60.67</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.53</td>
    <td align="right">62.59</td>
    <td align="right">62.40</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.70</td>
    <td align="right">37.07</td>
    <td align="right">25.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.41</td>
    <td align="right">84.24</td>
    <td align="right">83.79</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.19</td>
    <td align="right">82.22</td>
    <td align="right">82.66</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.20</td>
    <td align="right">55.22</td>
    <td align="right">39.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.04</td>
    <td align="right">93.45</td>
    <td align="right">93.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">52.03</td>
    <td align="right">97.98</td>
    <td align="right">98.59</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.29</td>
    <td align="right">56.23</td>
    <td align="right">41.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.86</td>
    <td align="right">26.45</td>
    <td align="right">26.53</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.69</td>
    <td align="right">29.57</td>
    <td align="right">29.35</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.90</td>
    <td align="right">31.25</td>
    <td align="right">31.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">21.33</td>
    <td align="right">46.87</td>
    <td align="right">35.01</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.69</td>
    <td align="right">40.76</td>
    <td align="right">27.98</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.51</td>
    <td align="right">52.77</td>
    <td align="right">39.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.71</td>
    <td align="right">54.95</td>
    <td align="right">38.98</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.27</td>
    <td align="right">53.40</td>
    <td align="right">35.52</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.33</td>
    <td align="right">61.44</td>
    <td align="right">43.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.76</td>
    <td align="right">55.28</td>
    <td align="right">39.57</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.87</td>
    <td align="right">64.72</td>
    <td align="right">44.78</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.23</td>
    <td align="right">63.88</td>
    <td align="right">44.88</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.96</td>
    <td align="right">34.99</td>
    <td align="right">11.18</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">67.28</td>
    <td align="right">59.84</td>
    <td align="right">46.47</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.39</td>
    <td align="right">21.85</td>
    <td align="right">33.63</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">30.00</td>
    <td align="right">29.49</td>
    <td align="right">33.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">101.69</td>
    <td align="right">107.76</td>
    <td align="right">53.51</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">35.75</td>
    <td align="right">23.19</td>
    <td align="right">27.66</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">33.72</td>
    <td align="right">35.03</td>
    <td align="right">38.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">152.73</td>
    <td align="right">121.60</td>
    <td align="right">55.53</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">32.07</td>
    <td align="right">28.12</td>
    <td align="right">33.77</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">46.50</td>
    <td align="right">49.26</td>
    <td align="right">40.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">196.65</td>
    <td align="right">216.06</td>
    <td align="right">67.01</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">33.74</td>
    <td align="right">28.83</td>
    <td align="right">31.33</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">47.80</td>
    <td align="right">80.51</td>
    <td align="right">56.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.89</td>
    <td align="right">46.38</td>
    <td align="right">48.59</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.77</td>
    <td align="right">46.44</td>
    <td align="right">49.00</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.10</td>
    <td align="right">30.09</td>
    <td align="right">31.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">37.09</td>
    <td align="right">76.69</td>
    <td align="right">73.11</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.91</td>
    <td align="right">68.64</td>
    <td align="right">75.95</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">23.11</td>
    <td align="right">53.75</td>
    <td align="right">35.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">48.14</td>
    <td align="right">88.14</td>
    <td align="right">87.50</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">57.75</td>
    <td align="right">90.68</td>
    <td align="right">103.45</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">41.35</td>
    <td align="right">71.90</td>
    <td align="right">49.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">60.09</td>
    <td align="right">105.63</td>
    <td align="right">105.52</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">68.18</td>
    <td align="right">116.67</td>
    <td align="right">117.98</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">76.29</td>
    <td align="right">126.09</td>
    <td align="right">85.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">21.71</td>
    <td align="right">32.49</td>
    <td align="right">32.65</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">30.95</td>
    <td align="right">38.67</td>
    <td align="right">43.15</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">24.24</td>
    <td align="right">38.87</td>
    <td align="right">37.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">25.53</td>
    <td align="right">58.12</td>
    <td align="right">44.08</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">21.15</td>
    <td align="right">47.33</td>
    <td align="right">33.34</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">25.74</td>
    <td align="right">60.60</td>
    <td align="right">43.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">30.66</td>
    <td align="right">60.02</td>
    <td align="right">43.31</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">34.41</td>
    <td align="right">56.06</td>
    <td align="right">40.34</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">33.06</td>
    <td align="right">64.49</td>
    <td align="right">46.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">35.57</td>
    <td align="right">65.13</td>
    <td align="right">48.51</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">38.30</td>
    <td align="right">73.67</td>
    <td align="right">58.61</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">43.60</td>
    <td align="right">71.70</td>
    <td align="right">52.20</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
