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
    <td align="right">26.03</td>
    <td align="right">4.53</td>
    <td align="right">3.51</td>
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
    <td align="right">12.20</td>
    <td align="right">10.63</td>
    <td align="right">16.55</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.03</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.80</td>
    <td align="right">5.03</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.62</td>
    <td align="right">15.75</td>
    <td align="right">17.69</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.82</td>
    <td align="right">4.96</td>
    <td align="right">4.98</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.45</td>
    <td align="right">5.52</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.13</td>
    <td align="right">18.76</td>
    <td align="right">16.60</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.40</td>
    <td align="right">5.34</td>
    <td align="right">5.33</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.30</td>
    <td align="right">6.33</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.59</td>
    <td align="right">23.01</td>
    <td align="right">16.88</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.41</td>
    <td align="right">6.09</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.73</td>
    <td align="right">6.61</td>
    <td align="right">6.62</td>
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
    <td align="right">5.72</td>
    <td align="right">5.72</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.55</td>
    <td align="right">6.69</td>
    <td align="right">6.86</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.99</td>
    <td align="right">3.29</td>
    <td align="right">3.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.07</td>
    <td align="right">8.88</td>
    <td align="right">8.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.22</td>
    <td align="right">10.07</td>
    <td align="right">10.08</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.49</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.36</td>
    <td align="right">13.90</td>
    <td align="right">13.79</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.71</td>
    <td align="right">14.17</td>
    <td align="right">14.17</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.73</td>
    <td align="right">5.85</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.18</td>
    <td align="right">15.49</td>
    <td align="right">15.51</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.08</td>
    <td align="right">17.44</td>
    <td align="right">17.38</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.75</td>
    <td align="right">5.78</td>
    <td align="right">3.89</td>
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
    <td align="right">2.95</td>
    <td align="right">3.24</td>
    <td align="right">3.23</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.38</td>
    <td align="right">5.10</td>
    <td align="right">5.03</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.52</td>
    <td align="right">4.95</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.06</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.43</td>
    <td align="right">5.10</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.44</td>
    <td align="right">5.51</td>
    <td align="right">3.78</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.03</td>
    <td align="right">7.69</td>
    <td align="right">5.88</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.95</td>
    <td align="right">7.58</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.45</td>
    <td align="right">5.52</td>
    <td align="right">3.75</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.10</td>
    <td align="right">9.16</td>
    <td align="right">6.07</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.38</td>
    <td align="right">9.05</td>
    <td align="right">5.90</td>
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
    <td align="right">31.39</td>
    <td align="right">18.30</td>
    <td align="right">6.92</td>
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
    <td align="right">13.15</td>
    <td align="right">12.49</td>
    <td align="right">17.33</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.61</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.59</td>
    <td align="right">5.78</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.76</td>
    <td align="right">18.25</td>
    <td align="right">17.98</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.24</td>
    <td align="right">5.32</td>
    <td align="right">5.37</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.93</td>
    <td align="right">5.96</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">26.45</td>
    <td align="right">19.23</td>
    <td align="right">18.46</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.37</td>
    <td align="right">6.30</td>
    <td align="right">6.65</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.37</td>
    <td align="right">8.00</td>
    <td align="right">8.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">41.59</td>
    <td align="right">37.26</td>
    <td align="right">19.38</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.55</td>
    <td align="right">9.46</td>
    <td align="right">9.45</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.35</td>
    <td align="right">9.57</td>
    <td align="right">9.39</td>
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
    <td align="right">5.82</td>
    <td align="right">6.63</td>
    <td align="right">6.66</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.33</td>
    <td align="right">7.73</td>
    <td align="right">7.98</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.47</td>
    <td align="right">3.93</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.75</td>
    <td align="right">9.71</td>
    <td align="right">12.46</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.01</td>
    <td align="right">11.15</td>
    <td align="right">11.21</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.92</td>
    <td align="right">3.48</td>
    <td align="right">3.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.99</td>
    <td align="right">23.67</td>
    <td align="right">18.75</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.92</td>
    <td align="right">19.45</td>
    <td align="right">15.69</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.04</td>
    <td align="right">7.87</td>
    <td align="right">7.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">15.19</td>
    <td align="right">21.94</td>
    <td align="right">20.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.10</td>
    <td align="right">24.80</td>
    <td align="right">26.94</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.19</td>
    <td align="right">13.27</td>
    <td align="right">7.67</td>
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
    <td align="right">3.44</td>
    <td align="right">3.88</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.09</td>
    <td align="right">5.89</td>
    <td align="right">5.85</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.13</td>
    <td align="right">5.62</td>
    <td align="right">5.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.39</td>
    <td align="right">3.78</td>
    <td align="right">3.94</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.56</td>
    <td align="right">4.88</td>
    <td align="right">4.91</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.93</td>
    <td align="right">5.63</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.96</td>
    <td align="right">7.24</td>
    <td align="right">5.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.58</td>
    <td align="right">9.98</td>
    <td align="right">7.78</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.80</td>
    <td align="right">10.84</td>
    <td align="right">9.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.74</td>
    <td align="right">11.62</td>
    <td align="right">6.77</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">14.76</td>
    <td align="right">15.18</td>
    <td align="right">9.02</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.85</td>
    <td align="right">14.91</td>
    <td align="right">10.34</td>
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
    <td align="right">26.82</td>
    <td align="right">4.11</td>
    <td align="right">3.39</td>
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
    <td align="right">9.05</td>
    <td align="right">15.62</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">4.07</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.88</td>
    <td align="right">4.59</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.00</td>
    <td align="right">13.72</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.85</td>
    <td align="right">4.73</td>
    <td align="right">4.57</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.53</td>
    <td align="right">5.32</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.43</td>
    <td align="right">16.80</td>
    <td align="right">15.86</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.35</td>
    <td align="right">5.26</td>
    <td align="right">5.10</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.92</td>
    <td align="right">5.98</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.06</td>
    <td align="right">22.61</td>
    <td align="right">15.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.80</td>
    <td align="right">5.68</td>
    <td align="right">5.69</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.01</td>
    <td align="right">3.31</td>
    <td align="right">3.31</td>
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
    <td align="right">3.07</td>
    <td align="right">3.59</td>
    <td align="right">3.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.16</td>
    <td align="right">3.54</td>
    <td align="right">3.58</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.61</td>
    <td align="right">2.52</td>
    <td align="right">2.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.74</td>
    <td align="right">3.39</td>
    <td align="right">3.42</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.75</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.17</td>
    <td align="right">2.29</td>
    <td align="right">2.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.57</td>
    <td align="right">6.15</td>
    <td align="right">6.44</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.88</td>
    <td align="right">6.16</td>
    <td align="right">6.14</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.20</td>
    <td align="right">4.38</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.11</td>
    <td align="right">6.72</td>
    <td align="right">6.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.36</td>
    <td align="right">7.26</td>
    <td align="right">7.05</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.25</td>
    <td align="right">4.40</td>
    <td align="right">3.19</td>
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
    <td align="right">2.62</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.60</td>
    <td align="right">4.08</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.73</td>
    <td align="right">3.94</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.73</td>
    <td align="right">2.43</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.92</td>
    <td align="right">3.73</td>
    <td align="right">3.74</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.92</td>
    <td align="right">4.03</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.26</td>
    <td align="right">4.29</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.60</td>
    <td align="right">6.18</td>
    <td align="right">4.74</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.74</td>
    <td align="right">6.02</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.30</td>
    <td align="right">4.33</td>
    <td align="right">2.98</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.78</td>
    <td align="right">7.14</td>
    <td align="right">4.87</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.84</td>
    <td align="right">7.14</td>
    <td align="right">4.74</td>
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
    <td align="right">32.08</td>
    <td align="right">16.16</td>
    <td align="right">6.48</td>
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
    <td align="right">11.20</td>
    <td align="right">11.00</td>
    <td align="right">16.66</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.05</td>
    <td align="right">4.80</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.78</td>
    <td align="right">5.45</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.05</td>
    <td align="right">15.77</td>
    <td align="right">17.18</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.51</td>
    <td align="right">5.35</td>
    <td align="right">5.19</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.97</td>
    <td align="right">5.73</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">20.61</td>
    <td align="right">20.13</td>
    <td align="right">16.96</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.34</td>
    <td align="right">6.16</td>
    <td align="right">6.33</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.28</td>
    <td align="right">7.43</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">32.88</td>
    <td align="right">32.53</td>
    <td align="right">17.38</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.91</td>
    <td align="right">7.47</td>
    <td align="right">8.46</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.48</td>
    <td align="right">5.16</td>
    <td align="right">5.17</td>
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
    <td align="right">3.80</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.87</td>
    <td align="right">4.37</td>
    <td align="right">4.43</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.20</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.30</td>
    <td align="right">3.95</td>
    <td align="right">3.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.24</td>
    <td align="right">4.53</td>
    <td align="right">4.72</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.61</td>
    <td align="right">2.78</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">7.18</td>
    <td align="right">7.95</td>
    <td align="right">8.06</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.74</td>
    <td align="right">8.07</td>
    <td align="right">7.90</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.45</td>
    <td align="right">5.63</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">8.30</td>
    <td align="right">9.39</td>
    <td align="right">9.51</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.71</td>
    <td align="right">10.36</td>
    <td align="right">10.27</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">6.55</td>
    <td align="right">7.16</td>
    <td align="right">5.34</td>
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
    <td align="right">3.09</td>
    <td align="right">3.14</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.40</td>
    <td align="right">5.03</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.49</td>
    <td align="right">4.92</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.20</td>
    <td align="right">3.12</td>
    <td align="right">3.17</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.51</td>
    <td align="right">4.43</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.52</td>
    <td align="right">4.89</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">5.51</td>
    <td align="right">6.17</td>
    <td align="right">4.63</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">7.21</td>
    <td align="right">8.10</td>
    <td align="right">6.56</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.18</td>
    <td align="right">7.84</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.41</td>
    <td align="right">8.19</td>
    <td align="right">5.61</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">11.25</td>
    <td align="right">11.03</td>
    <td align="right">7.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.44</td>
    <td align="right">10.43</td>
    <td align="right">7.82</td>
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
    <td align="right">24.97</td>
    <td align="right">7.03</td>
    <td align="right">4.11</td>
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
    <td align="right">9.69</td>
    <td align="right">5.74</td>
    <td align="right">14.01</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">2.47</td>
    <td align="right">1.95</td>
    <td align="right">1.55</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.78</td>
    <td align="right">2.13</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.15</td>
    <td align="right">7.78</td>
    <td align="right">12.70</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">2.87</td>
    <td align="right">2.78</td>
    <td align="right">1.77</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">2.81</td>
    <td align="right">2.20</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">21.82</td>
    <td align="right">11.30</td>
    <td align="right">15.34</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">2.19</td>
    <td align="right">2.55</td>
    <td align="right">1.72</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.45</td>
    <td align="right">2.14</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.14</td>
    <td align="right">13.63</td>
    <td align="right">13.56</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.42</td>
    <td align="right">2.55</td>
    <td align="right">2.29</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.16</td>
    <td align="right">2.04</td>
    <td align="right">2.28</td>
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
    <td align="right">2.67</td>
    <td align="right">2.55</td>
    <td align="right">2.83</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.96</td>
    <td align="right">2.22</td>
    <td align="right">2.11</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.61</td>
    <td align="right">2.70</td>
    <td align="right">2.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.89</td>
    <td align="right">2.43</td>
    <td align="right">2.86</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.35</td>
    <td align="right">3.04</td>
    <td align="right">2.54</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.74</td>
    <td align="right">1.95</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.28</td>
    <td align="right">4.39</td>
    <td align="right">3.42</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.85</td>
    <td align="right">5.10</td>
    <td align="right">5.96</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.06</td>
    <td align="right">3.41</td>
    <td align="right">2.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">7.17</td>
    <td align="right">6.34</td>
    <td align="right">5.55</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.13</td>
    <td align="right">5.82</td>
    <td align="right">5.61</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.28</td>
    <td align="right">3.71</td>
    <td align="right">3.10</td>
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
    <td align="right">4.11</td>
    <td align="right">3.04</td>
    <td align="right">2.25</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.04</td>
    <td align="right">2.12</td>
    <td align="right">1.87</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.25</td>
    <td align="right">2.12</td>
    <td align="right">1.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.40</td>
    <td align="right">1.75</td>
    <td align="right">2.39</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.37</td>
    <td align="right">3.53</td>
    <td align="right">2.58</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.18</td>
    <td align="right">2.62</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.97</td>
    <td align="right">3.28</td>
    <td align="right">2.42</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.53</td>
    <td align="right">3.58</td>
    <td align="right">3.88</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.59</td>
    <td align="right">4.33</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.34</td>
    <td align="right">5.69</td>
    <td align="right">2.73</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">8.78</td>
    <td align="right">5.03</td>
    <td align="right">6.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.88</td>
    <td align="right">6.85</td>
    <td align="right">5.21</td>
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
    <td align="right">36.72</td>
    <td align="right">19.28</td>
    <td align="right">10.52</td>
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
    <td align="right">14.28</td>
    <td align="right">14.33</td>
    <td align="right">25.91</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.22</td>
    <td align="right">5.75</td>
    <td align="right">5.28</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.54</td>
    <td align="right">5.58</td>
    <td align="right">5.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">44.61</td>
    <td align="right">35.80</td>
    <td align="right">30.28</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.05</td>
    <td align="right">9.33</td>
    <td align="right">9.36</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.70</td>
    <td align="right">10.20</td>
    <td align="right">9.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">63.19</td>
    <td align="right">54.92</td>
    <td align="right">32.10</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.90</td>
    <td align="right">12.93</td>
    <td align="right">11.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.37</td>
    <td align="right">11.59</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">98.71</td>
    <td align="right">69.48</td>
    <td align="right">31.41</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.05</td>
    <td align="right">14.36</td>
    <td align="right">14.10</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.67</td>
    <td align="right">12.08</td>
    <td align="right">12.02</td>
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
    <td align="right">5.54</td>
    <td align="right">5.50</td>
    <td align="right">6.86</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.28</td>
    <td align="right">5.29</td>
    <td align="right">6.54</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.56</td>
    <td align="right">7.05</td>
    <td align="right">7.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.31</td>
    <td align="right">11.69</td>
    <td align="right">12.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.96</td>
    <td align="right">11.77</td>
    <td align="right">13.56</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.66</td>
    <td align="right">8.53</td>
    <td align="right">8.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">22.28</td>
    <td align="right">15.68</td>
    <td align="right">16.53</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.16</td>
    <td align="right">17.81</td>
    <td align="right">17.43</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">16.15</td>
    <td align="right">18.26</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">25.84</td>
    <td align="right">20.89</td>
    <td align="right">19.44</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.76</td>
    <td align="right">13.97</td>
    <td align="right">13.95</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.55</td>
    <td align="right">10.39</td>
    <td align="right">7.72</td>
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
    <td align="right">2.53</td>
    <td align="right">2.60</td>
    <td align="right">3.13</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.76</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.80</td>
    <td align="right">2.65</td>
    <td align="right">2.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.90</td>
    <td align="right">5.93</td>
    <td align="right">5.20</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">5.56</td>
    <td align="right">4.82</td>
    <td align="right">7.76</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.36</td>
    <td align="right">7.89</td>
    <td align="right">12.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">12.93</td>
    <td align="right">10.39</td>
    <td align="right">7.50</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.48</td>
    <td align="right">8.97</td>
    <td align="right">8.90</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.70</td>
    <td align="right">10.65</td>
    <td align="right">8.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.60</td>
    <td align="right">10.37</td>
    <td align="right">7.11</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.59</td>
    <td align="right">13.48</td>
    <td align="right">13.71</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">14.89</td>
    <td align="right">13.92</td>
    <td align="right">14.99</td>
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
    <td align="right">35.38</td>
    <td align="right">5.62</td>
    <td align="right">3.71</td>
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
    <td align="right">12.04</td>
    <td align="right">12.37</td>
    <td align="right">16.95</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.40</td>
    <td align="right">4.28</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.97</td>
    <td align="right">5.28</td>
    <td align="right">5.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.34</td>
    <td align="right">17.76</td>
    <td align="right">17.59</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.90</td>
    <td align="right">4.92</td>
    <td align="right">4.76</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.02</td>
    <td align="right">5.97</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.60</td>
    <td align="right">21.48</td>
    <td align="right">16.72</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.57</td>
    <td align="right">5.35</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.34</td>
    <td align="right">6.55</td>
    <td align="right">6.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.15</td>
    <td align="right">27.65</td>
    <td align="right">17.27</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.91</td>
    <td align="right">5.91</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.45</td>
    <td align="right">7.39</td>
    <td align="right">7.38</td>
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
    <td align="right">7.93</td>
    <td align="right">5.56</td>
    <td align="right">5.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.69</td>
    <td align="right">5.61</td>
    <td align="right">5.62</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.40</td>
    <td align="right">3.96</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.11</td>
    <td align="right">8.52</td>
    <td align="right">8.49</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.29</td>
    <td align="right">7.86</td>
    <td align="right">7.88</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.86</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.23</td>
    <td align="right">10.94</td>
    <td align="right">11.03</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.09</td>
    <td align="right">10.46</td>
    <td align="right">10.74</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.98</td>
    <td align="right">7.01</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.59</td>
    <td align="right">13.96</td>
    <td align="right">13.91</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.85</td>
    <td align="right">13.50</td>
    <td align="right">13.56</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.08</td>
    <td align="right">7.20</td>
    <td align="right">5.32</td>
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
    <td align="right">3.91</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.51</td>
    <td align="right">5.53</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.64</td>
    <td align="right">5.52</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.30</td>
    <td align="right">5.54</td>
    <td align="right">4.66</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.77</td>
    <td align="right">5.77</td>
    <td align="right">5.02</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.92</td>
    <td align="right">7.02</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.09</td>
    <td align="right">6.86</td>
    <td align="right">5.12</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.99</td>
    <td align="right">9.35</td>
    <td align="right">7.54</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.63</td>
    <td align="right">9.23</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.13</td>
    <td align="right">6.91</td>
    <td align="right">5.05</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.36</td>
    <td align="right">10.72</td>
    <td align="right">7.80</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.31</td>
    <td align="right">10.50</td>
    <td align="right">7.58</td>
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
    <td align="right">43.04</td>
    <td align="right">21.32</td>
    <td align="right">7.82</td>
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
    <td align="right">14.54</td>
    <td align="right">13.15</td>
    <td align="right">17.73</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">9.03</td>
    <td align="right">4.93</td>
    <td align="right">4.87</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.03</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.68</td>
    <td align="right">19.51</td>
    <td align="right">18.67</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.92</td>
    <td align="right">5.19</td>
    <td align="right">5.38</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.53</td>
    <td align="right">6.60</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">38.62</td>
    <td align="right">38.87</td>
    <td align="right">19.40</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.44</td>
    <td align="right">8.77</td>
    <td align="right">7.61</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.32</td>
    <td align="right">9.04</td>
    <td align="right">9.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">72.47</td>
    <td align="right">84.12</td>
    <td align="right">27.22</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.52</td>
    <td align="right">15.42</td>
    <td align="right">12.84</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">19.01</td>
    <td align="right">17.41</td>
    <td align="right">21.04</td>
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
    <td align="right">9.49</td>
    <td align="right">6.45</td>
    <td align="right">6.34</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.65</td>
    <td align="right">6.39</td>
    <td align="right">6.34</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.80</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.82</td>
    <td align="right">10.82</td>
    <td align="right">10.65</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.04</td>
    <td align="right">9.18</td>
    <td align="right">8.98</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.44</td>
    <td align="right">6.00</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">24.23</td>
    <td align="right">16.06</td>
    <td align="right">15.70</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.80</td>
    <td align="right">16.25</td>
    <td align="right">16.10</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.26</td>
    <td align="right">13.83</td>
    <td align="right">8.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">30.21</td>
    <td align="right">26.56</td>
    <td align="right">26.57</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.02</td>
    <td align="right">30.23</td>
    <td align="right">25.73</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.23</td>
    <td align="right">18.75</td>
    <td align="right">15.72</td>
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
    <td align="right">3.63</td>
    <td align="right">4.16</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.05</td>
    <td align="right">5.89</td>
    <td align="right">5.91</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.17</td>
    <td align="right">5.91</td>
    <td align="right">5.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.94</td>
    <td align="right">6.35</td>
    <td align="right">6.55</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.31</td>
    <td align="right">6.41</td>
    <td align="right">5.79</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.96</td>
    <td align="right">9.05</td>
    <td align="right">7.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.75</td>
    <td align="right">12.52</td>
    <td align="right">7.68</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.61</td>
    <td align="right">12.86</td>
    <td align="right">9.89</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.49</td>
    <td align="right">12.06</td>
    <td align="right">9.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">12.33</td>
    <td align="right">17.88</td>
    <td align="right">14.80</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">18.13</td>
    <td align="right">23.13</td>
    <td align="right">14.86</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">17.81</td>
    <td align="right">20.09</td>
    <td align="right">13.38</td>
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
    <td align="right">62.05</td>
    <td align="right">30.13</td>
    <td align="right">14.17</td>
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
    <td align="right">27.48</td>
    <td align="right">42.11</td>
    <td align="right">36.64</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.57</td>
    <td align="right">16.03</td>
    <td align="right">16.00</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.13</td>
    <td align="right">19.69</td>
    <td align="right">19.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.16</td>
    <td align="right">63.90</td>
    <td align="right">41.30</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.33</td>
    <td align="right">19.41</td>
    <td align="right">19.32</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.21</td>
    <td align="right">18.65</td>
    <td align="right">18.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.02</td>
    <td align="right">78.22</td>
    <td align="right">38.54</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.27</td>
    <td align="right">18.44</td>
    <td align="right">18.44</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.18</td>
    <td align="right">18.29</td>
    <td align="right">18.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.83</td>
    <td align="right">97.11</td>
    <td align="right">37.78</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.29</td>
    <td align="right">18.85</td>
    <td align="right">18.86</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.06</td>
    <td align="right">20.05</td>
    <td align="right">20.09</td>
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
    <td align="right">16.27</td>
    <td align="right">20.64</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.79</td>
    <td align="right">22.30</td>
    <td align="right">22.32</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.78</td>
    <td align="right">13.79</td>
    <td align="right">13.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.43</td>
    <td align="right">26.84</td>
    <td align="right">26.77</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.70</td>
    <td align="right">29.20</td>
    <td align="right">29.26</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.90</td>
    <td align="right">15.96</td>
    <td align="right">15.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.35</td>
    <td align="right">33.42</td>
    <td align="right">33.48</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.96</td>
    <td align="right">45.99</td>
    <td align="right">46.03</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.56</td>
    <td align="right">19.59</td>
    <td align="right">19.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.64</td>
    <td align="right">36.15</td>
    <td align="right">36.19</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.87</td>
    <td align="right">55.86</td>
    <td align="right">55.92</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.65</td>
    <td align="right">24.96</td>
    <td align="right">24.95</td>
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
    <td align="right">14.67</td>
    <td align="right">16.09</td>
    <td align="right">15.76</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.43</td>
    <td align="right">20.55</td>
    <td align="right">20.56</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.70</td>
    <td align="right">22.16</td>
    <td align="right">22.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.12</td>
    <td align="right">20.22</td>
    <td align="right">20.24</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.39</td>
    <td align="right">26.87</td>
    <td align="right">26.81</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.72</td>
    <td align="right">29.25</td>
    <td align="right">29.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.94</td>
    <td align="right">25.28</td>
    <td align="right">25.07</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.42</td>
    <td align="right">33.54</td>
    <td align="right">33.47</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.85</td>
    <td align="right">45.98</td>
    <td align="right">46.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">34.25</td>
    <td align="right">35.18</td>
    <td align="right">35.21</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.73</td>
    <td align="right">36.27</td>
    <td align="right">36.22</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.80</td>
    <td align="right">55.88</td>
    <td align="right">55.90</td>
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
    <td align="right">75.32</td>
    <td align="right">107.50</td>
    <td align="right">21.07</td>
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
    <td align="right">27.83</td>
    <td align="right">43.04</td>
    <td align="right">39.55</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.83</td>
    <td align="right">16.26</td>
    <td align="right">16.17</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.38</td>
    <td align="right">19.95</td>
    <td align="right">19.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">37.61</td>
    <td align="right">64.46</td>
    <td align="right">43.32</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.92</td>
    <td align="right">20.51</td>
    <td align="right">20.98</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.47</td>
    <td align="right">18.94</td>
    <td align="right">19.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">61.23</td>
    <td align="right">83.30</td>
    <td align="right">42.39</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">20.97</td>
    <td align="right">23.21</td>
    <td align="right">21.26</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">20.46</td>
    <td align="right">24.75</td>
    <td align="right">24.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">83.01</td>
    <td align="right">126.77</td>
    <td align="right">48.99</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">25.08</td>
    <td align="right">30.55</td>
    <td align="right">30.58</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">35.23</td>
    <td align="right">32.92</td>
    <td align="right">29.62</td>
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
    <td align="right">16.63</td>
    <td align="right">20.66</td>
    <td align="right">20.65</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.04</td>
    <td align="right">22.61</td>
    <td align="right">22.61</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.93</td>
    <td align="right">14.01</td>
    <td align="right">14.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.59</td>
    <td align="right">26.75</td>
    <td align="right">26.93</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">42.84</td>
    <td align="right">30.80</td>
    <td align="right">30.74</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.77</td>
    <td align="right">16.13</td>
    <td align="right">16.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">32.22</td>
    <td align="right">51.34</td>
    <td align="right">49.76</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">78.60</td>
    <td align="right">53.10</td>
    <td align="right">54.82</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">19.62</td>
    <td align="right">27.08</td>
    <td align="right">26.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.13</td>
    <td align="right">50.94</td>
    <td align="right">66.70</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">99.11</td>
    <td align="right">72.24</td>
    <td align="right">71.63</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">43.68</td>
    <td align="right">41.89</td>
    <td align="right">41.83</td>
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
    <td align="right">15.31</td>
    <td align="right">16.58</td>
    <td align="right">16.12</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.62</td>
    <td align="right">20.72</td>
    <td align="right">20.67</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.16</td>
    <td align="right">22.56</td>
    <td align="right">22.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">19.39</td>
    <td align="right">20.96</td>
    <td align="right">20.64</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.41</td>
    <td align="right">28.91</td>
    <td align="right">29.41</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">44.81</td>
    <td align="right">31.23</td>
    <td align="right">31.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">38.35</td>
    <td align="right">31.84</td>
    <td align="right">35.88</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.96</td>
    <td align="right">44.34</td>
    <td align="right">41.49</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">69.78</td>
    <td align="right">50.71</td>
    <td align="right">49.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">64.06</td>
    <td align="right">68.08</td>
    <td align="right">69.25</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.07</td>
    <td align="right">48.29</td>
    <td align="right">63.12</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">98.93</td>
    <td align="right">71.76</td>
    <td align="right">73.55</td>
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
    <td align="right">62.35</td>
    <td align="right">10.17</td>
    <td align="right">7.06</td>
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
    <td align="right">13.85</td>
    <td align="right">22.76</td>
    <td align="right">26.57</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.57</td>
    <td align="right">12.38</td>
    <td align="right">12.38</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.75</td>
    <td align="right">13.84</td>
    <td align="right">13.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.45</td>
    <td align="right">36.45</td>
    <td align="right">28.77</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.00</td>
    <td align="right">14.56</td>
    <td align="right">14.05</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.50</td>
    <td align="right">15.27</td>
    <td align="right">15.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.91</td>
    <td align="right">47.48</td>
    <td align="right">30.21</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.83</td>
    <td align="right">15.38</td>
    <td align="right">15.48</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.60</td>
    <td align="right">16.72</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.18</td>
    <td align="right">60.36</td>
    <td align="right">30.89</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.52</td>
    <td align="right">16.26</td>
    <td align="right">16.26</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.90</td>
    <td align="right">17.86</td>
    <td align="right">17.86</td>
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
    <td align="right">12.70</td>
    <td align="right">16.05</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.27</td>
    <td align="right">16.70</td>
    <td align="right">16.72</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.10</td>
    <td align="right">9.34</td>
    <td align="right">9.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.35</td>
    <td align="right">22.43</td>
    <td align="right">22.47</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.42</td>
    <td align="right">22.39</td>
    <td align="right">22.39</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.09</td>
    <td align="right">13.98</td>
    <td align="right">13.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.11</td>
    <td align="right">32.07</td>
    <td align="right">32.00</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.69</td>
    <td align="right">30.58</td>
    <td align="right">30.56</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.93</td>
    <td align="right">17.62</td>
    <td align="right">17.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.95</td>
    <td align="right">35.63</td>
    <td align="right">35.65</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.93</td>
    <td align="right">35.88</td>
    <td align="right">35.80</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.43</td>
    <td align="right">20.53</td>
    <td align="right">20.58</td>
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
    <td align="right">6.59</td>
    <td align="right">9.38</td>
    <td align="right">9.35</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.66</td>
    <td align="right">16.10</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.69</td>
    <td align="right">16.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.83</td>
    <td align="right">13.67</td>
    <td align="right">13.68</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.33</td>
    <td align="right">22.42</td>
    <td align="right">22.44</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.42</td>
    <td align="right">22.40</td>
    <td align="right">22.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.34</td>
    <td align="right">17.60</td>
    <td align="right">17.61</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.10</td>
    <td align="right">32.01</td>
    <td align="right">32.05</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.62</td>
    <td align="right">30.54</td>
    <td align="right">30.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.21</td>
    <td align="right">21.01</td>
    <td align="right">20.95</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.95</td>
    <td align="right">35.63</td>
    <td align="right">35.58</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.86</td>
    <td align="right">35.76</td>
    <td align="right">35.79</td>
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
    <td align="right">75.97</td>
    <td align="right">44.47</td>
    <td align="right">10.45</td>
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
    <td align="right">14.32</td>
    <td align="right">23.39</td>
    <td align="right">28.54</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.77</td>
    <td align="right">12.72</td>
    <td align="right">12.74</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.07</td>
    <td align="right">14.16</td>
    <td align="right">14.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.39</td>
    <td align="right">34.82</td>
    <td align="right">29.31</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.91</td>
    <td align="right">13.87</td>
    <td align="right">13.90</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.38</td>
    <td align="right">15.08</td>
    <td align="right">15.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.80</td>
    <td align="right">47.70</td>
    <td align="right">30.67</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.86</td>
    <td align="right">15.96</td>
    <td align="right">15.24</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.27</td>
    <td align="right">18.33</td>
    <td align="right">16.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">32.65</td>
    <td align="right">65.16</td>
    <td align="right">31.50</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">15.44</td>
    <td align="right">17.33</td>
    <td align="right">16.82</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">17.11</td>
    <td align="right">19.13</td>
    <td align="right">22.55</td>
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
    <td align="right">13.47</td>
    <td align="right">17.10</td>
    <td align="right">17.07</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.65</td>
    <td align="right">17.98</td>
    <td align="right">18.43</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.50</td>
    <td align="right">9.75</td>
    <td align="right">9.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">19.64</td>
    <td align="right">23.50</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.53</td>
    <td align="right">22.33</td>
    <td align="right">23.82</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.37</td>
    <td align="right">14.52</td>
    <td align="right">15.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.02</td>
    <td align="right">46.69</td>
    <td align="right">41.98</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">30.22</td>
    <td align="right">34.62</td>
    <td align="right">34.31</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">20.31</td>
    <td align="right">24.45</td>
    <td align="right">24.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">49.66</td>
    <td align="right">60.08</td>
    <td align="right">62.32</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">63.87</td>
    <td align="right">59.75</td>
    <td align="right">56.95</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">41.66</td>
    <td align="right">47.51</td>
    <td align="right">46.24</td>
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
    <td align="right">6.84</td>
    <td align="right">9.85</td>
    <td align="right">9.83</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.45</td>
    <td align="right">17.23</td>
    <td align="right">17.47</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.74</td>
    <td align="right">18.24</td>
    <td align="right">17.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">10.73</td>
    <td align="right">13.86</td>
    <td align="right">13.77</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">18.32</td>
    <td align="right">24.34</td>
    <td align="right">24.27</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.87</td>
    <td align="right">23.66</td>
    <td align="right">23.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">15.10</td>
    <td align="right">24.67</td>
    <td align="right">19.24</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.28</td>
    <td align="right">40.13</td>
    <td align="right">44.19</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">45.06</td>
    <td align="right">34.58</td>
    <td align="right">34.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">21.29</td>
    <td align="right">25.48</td>
    <td align="right">25.10</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">30.36</td>
    <td align="right">40.08</td>
    <td align="right">40.85</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">37.53</td>
    <td align="right">37.64</td>
    <td align="right">38.10</td>
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
    <td align="right">42.33</td>
    <td align="right">8.51</td>
    <td align="right">6.54</td>
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
    <td align="right">59.33</td>
    <td align="right">55.09</td>
    <td align="right">41.52</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.99</td>
    <td align="right">20.41</td>
    <td align="right">24.74</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">27.05</td>
    <td align="right">25.90</td>
    <td align="right">29.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.86</td>
    <td align="right">85.77</td>
    <td align="right">46.43</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.87</td>
    <td align="right">21.90</td>
    <td align="right">24.10</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">26.81</td>
    <td align="right">28.14</td>
    <td align="right">30.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.58</td>
    <td align="right">98.00</td>
    <td align="right">43.02</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.68</td>
    <td align="right">22.97</td>
    <td align="right">24.31</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.40</td>
    <td align="right">30.83</td>
    <td align="right">31.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.47</td>
    <td align="right">128.11</td>
    <td align="right">46.17</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.34</td>
    <td align="right">24.30</td>
    <td align="right">25.16</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.98</td>
    <td align="right">32.29</td>
    <td align="right">33.81</td>
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
    <td align="right">23.65</td>
    <td align="right">45.37</td>
    <td align="right">45.78</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.22</td>
    <td align="right">45.95</td>
    <td align="right">46.14</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.71</td>
    <td align="right">24.84</td>
    <td align="right">24.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.28</td>
    <td align="right">60.97</td>
    <td align="right">60.61</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.13</td>
    <td align="right">61.93</td>
    <td align="right">62.37</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.57</td>
    <td align="right">36.91</td>
    <td align="right">25.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.24</td>
    <td align="right">81.72</td>
    <td align="right">81.11</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.11</td>
    <td align="right">82.24</td>
    <td align="right">82.99</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.09</td>
    <td align="right">54.90</td>
    <td align="right">39.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.68</td>
    <td align="right">93.63</td>
    <td align="right">93.87</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.42</td>
    <td align="right">97.96</td>
    <td align="right">98.43</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.20</td>
    <td align="right">55.82</td>
    <td align="right">40.47</td>
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
    <td align="right">18.65</td>
    <td align="right">26.32</td>
    <td align="right">26.21</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.72</td>
    <td align="right">29.24</td>
    <td align="right">29.19</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.90</td>
    <td align="right">31.11</td>
    <td align="right">31.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">21.03</td>
    <td align="right">46.69</td>
    <td align="right">34.80</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.42</td>
    <td align="right">40.18</td>
    <td align="right">27.55</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.08</td>
    <td align="right">52.33</td>
    <td align="right">39.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.62</td>
    <td align="right">55.01</td>
    <td align="right">38.78</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.96</td>
    <td align="right">56.23</td>
    <td align="right">35.27</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.44</td>
    <td align="right">61.80</td>
    <td align="right">43.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.88</td>
    <td align="right">55.56</td>
    <td align="right">39.93</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.73</td>
    <td align="right">64.31</td>
    <td align="right">44.42</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.54</td>
    <td align="right">64.31</td>
    <td align="right">44.46</td>
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
    <td align="right">66.68</td>
    <td align="right">36.71</td>
    <td align="right">12.31</td>
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
    <td align="right">67.71</td>
    <td align="right">60.08</td>
    <td align="right">46.45</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">24.95</td>
    <td align="right">22.35</td>
    <td align="right">28.47</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">38.41</td>
    <td align="right">38.24</td>
    <td align="right">39.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">110.39</td>
    <td align="right">103.31</td>
    <td align="right">56.03</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.11</td>
    <td align="right">25.45</td>
    <td align="right">27.88</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">34.38</td>
    <td align="right">36.85</td>
    <td align="right">39.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">206.25</td>
    <td align="right">145.94</td>
    <td align="right">87.52</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">41.32</td>
    <td align="right">35.55</td>
    <td align="right">50.15</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">64.06</td>
    <td align="right">80.17</td>
    <td align="right">80.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">486.58</td>
    <td align="right">244.81</td>
    <td align="right">66.42</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">45.62</td>
    <td align="right">41.58</td>
    <td align="right">38.90</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">53.44</td>
    <td align="right">58.18</td>
    <td align="right">56.29</td>
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
    <td align="right">25.90</td>
    <td align="right">46.37</td>
    <td align="right">47.00</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.02</td>
    <td align="right">47.75</td>
    <td align="right">47.64</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.08</td>
    <td align="right">29.75</td>
    <td align="right">29.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">32.93</td>
    <td align="right">65.51</td>
    <td align="right">65.60</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">41.06</td>
    <td align="right">68.13</td>
    <td align="right">68.15</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.87</td>
    <td align="right">43.35</td>
    <td align="right">30.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.58</td>
    <td align="right">89.39</td>
    <td align="right">88.53</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">53.02</td>
    <td align="right">90.95</td>
    <td align="right">90.91</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">44.53</td>
    <td align="right">79.62</td>
    <td align="right">58.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">57.90</td>
    <td align="right">106.81</td>
    <td align="right">108.04</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">67.59</td>
    <td align="right">118.83</td>
    <td align="right">115.16</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">54.39</td>
    <td align="right">99.49</td>
    <td align="right">75.79</td>
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
    <td align="right">19.95</td>
    <td align="right">31.58</td>
    <td align="right">31.30</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.95</td>
    <td align="right">34.55</td>
    <td align="right">33.52</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">22.33</td>
    <td align="right">36.49</td>
    <td align="right">36.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">22.56</td>
    <td align="right">54.00</td>
    <td align="right">41.08</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">21.89</td>
    <td align="right">45.96</td>
    <td align="right">31.31</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">23.92</td>
    <td align="right">65.44</td>
    <td align="right">58.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">46.75</td>
    <td align="right">77.76</td>
    <td align="right">59.99</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">38.80</td>
    <td align="right">65.68</td>
    <td align="right">46.18</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">38.65</td>
    <td align="right">72.42</td>
    <td align="right">52.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">62.41</td>
    <td align="right">94.04</td>
    <td align="right">74.99</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">42.93</td>
    <td align="right">92.96</td>
    <td align="right">72.62</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">44.29</td>
    <td align="right">84.64</td>
    <td align="right">62.41</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
