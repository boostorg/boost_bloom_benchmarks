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
    <td align="right">26.29</td>
    <td align="right">4.57</td>
    <td align="right">3.52</td>
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
    <td align="right">11.04</td>
    <td align="right">11.03</td>
    <td align="right">16.61</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.87</td>
    <td align="right">4.21</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.85</td>
    <td align="right">5.08</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.32</td>
    <td align="right">15.48</td>
    <td align="right">17.51</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.78</td>
    <td align="right">4.90</td>
    <td align="right">4.93</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.49</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.82</td>
    <td align="right">18.23</td>
    <td align="right">16.42</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.39</td>
    <td align="right">5.29</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.22</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.06</td>
    <td align="right">23.27</td>
    <td align="right">16.79</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.17</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.69</td>
    <td align="right">6.57</td>
    <td align="right">6.59</td>
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
    <td align="right">5.10</td>
    <td align="right">5.72</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.22</td>
    <td align="right">6.50</td>
    <td align="right">6.43</td>
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
    <td align="right">6.51</td>
    <td align="right">8.85</td>
    <td align="right">8.84</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.12</td>
    <td align="right">9.79</td>
    <td align="right">9.80</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.15</td>
    <td align="right">13.67</td>
    <td align="right">13.67</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.76</td>
    <td align="right">13.94</td>
    <td align="right">13.95</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.71</td>
    <td align="right">5.75</td>
    <td align="right">3.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">10.94</td>
    <td align="right">15.32</td>
    <td align="right">15.31</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.09</td>
    <td align="right">17.29</td>
    <td align="right">17.28</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.77</td>
    <td align="right">5.77</td>
    <td align="right">3.87</td>
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
    <td align="right">2.93</td>
    <td align="right">3.22</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.42</td>
    <td align="right">5.10</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.58</td>
    <td align="right">4.96</td>
    <td align="right">5.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.06</td>
    <td align="right">3.32</td>
    <td align="right">3.31</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.19</td>
    <td align="right">4.45</td>
    <td align="right">4.43</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.44</td>
    <td align="right">5.10</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.43</td>
    <td align="right">5.46</td>
    <td align="right">3.75</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.05</td>
    <td align="right">7.70</td>
    <td align="right">5.88</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.89</td>
    <td align="right">7.58</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.45</td>
    <td align="right">5.48</td>
    <td align="right">3.79</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.08</td>
    <td align="right">9.15</td>
    <td align="right">5.99</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.35</td>
    <td align="right">9.00</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.89</td>
    <td align="right">6.97</td>
    <td align="right">13.54</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.39</td>
    <td align="right">8.94</td>
    <td align="right">17.34</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.56</td>
    <td align="right">11.48</td>
    <td align="right">11.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.31</td>
    <td align="right">8.32</td>
    <td align="right">12.35</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.11</td>
    <td align="right">9.45</td>
    <td align="right">14.25</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.00</td>
    <td align="right">15.34</td>
    <td align="right">15.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.93</td>
    <td align="right">10.36</td>
    <td align="right">12.04</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.32</td>
    <td align="right">12.59</td>
    <td align="right">15.20</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">18.54</td>
    <td align="right">18.57</td>
    <td align="right">18.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.40</td>
    <td align="right">12.72</td>
    <td align="right">13.13</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.75</td>
    <td align="right">14.12</td>
    <td align="right">14.86</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">25.42</td>
    <td align="right">25.19</td>
    <td align="right">25.25</td>
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
    <td align="right">30.32</td>
    <td align="right">16.98</td>
    <td align="right">6.43</td>
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
    <td align="right">13.09</td>
    <td align="right">12.31</td>
    <td align="right">17.92</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.17</td>
    <td align="right">5.32</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.03</td>
    <td align="right">6.27</td>
    <td align="right">6.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">29.17</td>
    <td align="right">31.47</td>
    <td align="right">21.09</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">14.84</td>
    <td align="right">13.67</td>
    <td align="right">11.98</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.86</td>
    <td align="right">5.99</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">29.13</td>
    <td align="right">28.56</td>
    <td align="right">18.78</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.94</td>
    <td align="right">9.93</td>
    <td align="right">10.96</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.02</td>
    <td align="right">13.65</td>
    <td align="right">12.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">52.29</td>
    <td align="right">50.18</td>
    <td align="right">19.82</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.11</td>
    <td align="right">11.68</td>
    <td align="right">11.22</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">22.33</td>
    <td align="right">20.66</td>
    <td align="right">20.39</td>
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
    <td align="right">5.96</td>
    <td align="right">6.89</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.15</td>
    <td align="right">7.75</td>
    <td align="right">7.80</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.43</td>
    <td align="right">3.91</td>
    <td align="right">3.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.62</td>
    <td align="right">13.24</td>
    <td align="right">13.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.75</td>
    <td align="right">17.76</td>
    <td align="right">15.10</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.23</td>
    <td align="right">4.87</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.28</td>
    <td align="right">19.96</td>
    <td align="right">20.49</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.50</td>
    <td align="right">23.75</td>
    <td align="right">24.01</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">18.22</td>
    <td align="right">19.09</td>
    <td align="right">11.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">35.35</td>
    <td align="right">34.55</td>
    <td align="right">34.98</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">46.34</td>
    <td align="right">48.78</td>
    <td align="right">39.77</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">62.70</td>
    <td align="right">19.84</td>
    <td align="right">12.91</td>
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
    <td align="right">3.46</td>
    <td align="right">3.95</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">6.52</td>
    <td align="right">5.97</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">7.20</td>
    <td align="right">5.86</td>
    <td align="right">6.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.72</td>
    <td align="right">5.41</td>
    <td align="right">8.99</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">11.92</td>
    <td align="right">14.55</td>
    <td align="right">6.58</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.29</td>
    <td align="right">8.88</td>
    <td align="right">8.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">13.55</td>
    <td align="right">14.72</td>
    <td align="right">9.46</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">13.82</td>
    <td align="right">18.00</td>
    <td align="right">13.49</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.49</td>
    <td align="right">20.17</td>
    <td align="right">14.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">29.92</td>
    <td align="right">19.16</td>
    <td align="right">12.27</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">23.58</td>
    <td align="right">28.85</td>
    <td align="right">19.83</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">22.01</td>
    <td align="right">30.40</td>
    <td align="right">22.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">13.37</td>
    <td align="right">21.96</td>
    <td align="right">20.91</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">32.35</td>
    <td align="right">11.82</td>
    <td align="right">20.25</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.70</td>
    <td align="right">13.51</td>
    <td align="right">13.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.74</td>
    <td align="right">10.51</td>
    <td align="right">13.27</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.67</td>
    <td align="right">11.81</td>
    <td align="right">15.02</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.09</td>
    <td align="right">17.72</td>
    <td align="right">17.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">20.78</td>
    <td align="right">18.32</td>
    <td align="right">15.45</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">25.47</td>
    <td align="right">20.81</td>
    <td align="right">17.87</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">20.91</td>
    <td align="right">21.98</td>
    <td align="right">22.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">36.65</td>
    <td align="right">28.86</td>
    <td align="right">19.24</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">47.25</td>
    <td align="right">31.60</td>
    <td align="right">20.45</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">32.54</td>
    <td align="right">33.90</td>
    <td align="right">52.37</td>
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
    <td align="right">27.82</td>
    <td align="right">4.94</td>
    <td align="right">3.80</td>
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
    <td align="right">8.81</td>
    <td align="right">8.27</td>
    <td align="right">14.78</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.22</td>
    <td align="right">3.80</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.80</td>
    <td align="right">4.49</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.59</td>
    <td align="right">12.56</td>
    <td align="right">15.96</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.73</td>
    <td align="right">4.41</td>
    <td align="right">4.55</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.40</td>
    <td align="right">5.35</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.47</td>
    <td align="right">15.11</td>
    <td align="right">15.00</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.19</td>
    <td align="right">4.90</td>
    <td align="right">4.94</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.91</td>
    <td align="right">5.92</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.32</td>
    <td align="right">18.84</td>
    <td align="right">15.46</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.84</td>
    <td align="right">5.57</td>
    <td align="right">5.57</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.71</td>
    <td align="right">3.11</td>
    <td align="right">3.09</td>
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
    <td align="right">2.96</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.05</td>
    <td align="right">3.35</td>
    <td align="right">3.34</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.49</td>
    <td align="right">2.39</td>
    <td align="right">2.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.58</td>
    <td align="right">3.93</td>
    <td align="right">3.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.50</td>
    <td align="right">4.21</td>
    <td align="right">4.20</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.03</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.34</td>
    <td align="right">7.19</td>
    <td align="right">6.74</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.51</td>
    <td align="right">6.57</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.97</td>
    <td align="right">4.20</td>
    <td align="right">3.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.74</td>
    <td align="right">7.40</td>
    <td align="right">7.45</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.04</td>
    <td align="right">7.79</td>
    <td align="right">7.74</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.02</td>
    <td align="right">4.21</td>
    <td align="right">2.97</td>
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
    <td align="right">2.48</td>
    <td align="right">2.23</td>
    <td align="right">2.23</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.43</td>
    <td align="right">3.90</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.58</td>
    <td align="right">3.77</td>
    <td align="right">3.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.54</td>
    <td align="right">2.30</td>
    <td align="right">2.28</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.73</td>
    <td align="right">3.57</td>
    <td align="right">3.58</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.62</td>
    <td align="right">3.83</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.04</td>
    <td align="right">4.07</td>
    <td align="right">2.78</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.27</td>
    <td align="right">5.85</td>
    <td align="right">4.71</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.46</td>
    <td align="right">5.70</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.05</td>
    <td align="right">4.08</td>
    <td align="right">2.77</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.45</td>
    <td align="right">6.81</td>
    <td align="right">5.40</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.59</td>
    <td align="right">6.79</td>
    <td align="right">4.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">6.46</td>
    <td align="right">5.79</td>
    <td align="right">11.88</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.16</td>
    <td align="right">7.76</td>
    <td align="right">16.31</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.30</td>
    <td align="right">10.55</td>
    <td align="right">10.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.02</td>
    <td align="right">7.73</td>
    <td align="right">11.72</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">11.75</td>
    <td align="right">9.23</td>
    <td align="right">13.84</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">16.36</td>
    <td align="right">16.64</td>
    <td align="right">16.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.13</td>
    <td align="right">9.66</td>
    <td align="right">11.77</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.52</td>
    <td align="right">12.29</td>
    <td align="right">14.59</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">18.09</td>
    <td align="right">17.40</td>
    <td align="right">17.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.08</td>
    <td align="right">11.51</td>
    <td align="right">12.35</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.32</td>
    <td align="right">13.55</td>
    <td align="right">14.39</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">24.71</td>
    <td align="right">23.45</td>
    <td align="right">24.65</td>
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
    <td align="right">35.76</td>
    <td align="right">17.72</td>
    <td align="right">8.58</td>
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
    <td align="right">11.24</td>
    <td align="right">11.86</td>
    <td align="right">16.34</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.98</td>
    <td align="right">4.52</td>
    <td align="right">4.72</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.61</td>
    <td align="right">5.44</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">17.80</td>
    <td align="right">22.76</td>
    <td align="right">19.70</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.92</td>
    <td align="right">6.94</td>
    <td align="right">7.52</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.59</td>
    <td align="right">9.52</td>
    <td align="right">6.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">41.38</td>
    <td align="right">50.27</td>
    <td align="right">20.92</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.56</td>
    <td align="right">11.11</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">8.89</td>
    <td align="right">9.64</td>
    <td align="right">10.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">76.52</td>
    <td align="right">67.48</td>
    <td align="right">27.27</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.33</td>
    <td align="right">16.01</td>
    <td align="right">15.93</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.72</td>
    <td align="right">10.11</td>
    <td align="right">9.38</td>
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
    <td align="right">3.47</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.72</td>
    <td align="right">4.15</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.03</td>
    <td align="right">2.98</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.76</td>
    <td align="right">6.27</td>
    <td align="right">5.98</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.70</td>
    <td align="right">5.62</td>
    <td align="right">5.43</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.76</td>
    <td align="right">3.06</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.45</td>
    <td align="right">11.76</td>
    <td align="right">10.87</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.33</td>
    <td align="right">8.73</td>
    <td align="right">9.54</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.25</td>
    <td align="right">10.04</td>
    <td align="right">7.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">12.72</td>
    <td align="right">15.95</td>
    <td align="right">15.17</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">12.12</td>
    <td align="right">17.16</td>
    <td align="right">17.75</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">12.29</td>
    <td align="right">13.31</td>
    <td align="right">10.01</td>
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
    <td align="right">3.00</td>
    <td align="right">2.82</td>
    <td align="right">2.76</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.26</td>
    <td align="right">4.96</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.34</td>
    <td align="right">4.59</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.14</td>
    <td align="right">2.80</td>
    <td align="right">2.81</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.41</td>
    <td align="right">4.96</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.90</td>
    <td align="right">5.35</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.20</td>
    <td align="right">10.25</td>
    <td align="right">5.19</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.38</td>
    <td align="right">9.27</td>
    <td align="right">7.59</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">8.50</td>
    <td align="right">9.56</td>
    <td align="right">7.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.85</td>
    <td align="right">12.96</td>
    <td align="right">8.72</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">13.08</td>
    <td align="right">15.32</td>
    <td align="right">9.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.35</td>
    <td align="right">16.96</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">7.92</td>
    <td align="right">7.71</td>
    <td align="right">13.29</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.76</td>
    <td align="right">9.37</td>
    <td align="right">18.08</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.22</td>
    <td align="right">13.23</td>
    <td align="right">13.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">12.96</td>
    <td align="right">10.10</td>
    <td align="right">14.57</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">17.90</td>
    <td align="right">13.14</td>
    <td align="right">16.02</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.71</td>
    <td align="right">17.91</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">29.10</td>
    <td align="right">23.40</td>
    <td align="right">16.46</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">36.63</td>
    <td align="right">30.82</td>
    <td align="right">20.34</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">24.26</td>
    <td align="right">24.68</td>
    <td align="right">25.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">40.56</td>
    <td align="right">31.74</td>
    <td align="right">18.63</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">52.51</td>
    <td align="right">36.46</td>
    <td align="right">20.49</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">34.31</td>
    <td align="right">35.98</td>
    <td align="right">35.34</td>
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
    <td align="right">22.33</td>
    <td align="right">2.54</td>
    <td align="right">1.96</td>
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
    <td align="right">6.27</td>
    <td align="right">8.21</td>
    <td align="right">12.61</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.39</td>
    <td align="right">1.22</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.80</td>
    <td align="right">2.36</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.64</td>
    <td align="right">8.23</td>
    <td align="right">13.29</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.45</td>
    <td align="right">1.46</td>
    <td align="right">1.50</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.95</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">14.41</td>
    <td align="right">9.37</td>
    <td align="right">12.17</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.90</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.94</td>
    <td align="right">12.39</td>
    <td align="right">12.31</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.91</td>
    <td align="right">1.86</td>
    <td align="right">2.12</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.96</td>
    <td align="right">1.74</td>
    <td align="right">1.68</td>
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
    <td align="right">2.35</td>
    <td align="right">1.84</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">1.90</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.16</td>
    <td align="right">1.87</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.43</td>
    <td align="right">2.21</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.97</td>
    <td align="right">2.34</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.57</td>
    <td align="right">1.45</td>
    <td align="right">1.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.25</td>
    <td align="right">3.32</td>
    <td align="right">3.19</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.47</td>
    <td align="right">3.18</td>
    <td align="right">3.05</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.91</td>
    <td align="right">2.50</td>
    <td align="right">2.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.11</td>
    <td align="right">4.02</td>
    <td align="right">3.76</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.81</td>
    <td align="right">5.01</td>
    <td align="right">4.33</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.98</td>
    <td align="right">2.89</td>
    <td align="right">1.74</td>
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
    <td align="right">2.71</td>
    <td align="right">1.89</td>
    <td align="right">1.92</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.34</td>
    <td align="right">1.72</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.53</td>
    <td align="right">1.94</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.07</td>
    <td align="right">1.80</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.17</td>
    <td align="right">2.15</td>
    <td align="right">2.23</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.87</td>
    <td align="right">5.34</td>
    <td align="right">2.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.25</td>
    <td align="right">2.69</td>
    <td align="right">1.95</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.43</td>
    <td align="right">2.91</td>
    <td align="right">3.40</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.49</td>
    <td align="right">3.23</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.00</td>
    <td align="right">3.90</td>
    <td align="right">1.98</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.21</td>
    <td align="right">3.96</td>
    <td align="right">3.98</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.62</td>
    <td align="right">4.34</td>
    <td align="right">4.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">3.71</td>
    <td align="right">3.56</td>
    <td align="right">11.38</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.92</td>
    <td align="right">4.26</td>
    <td align="right">14.05</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">7.95</td>
    <td align="right">5.42</td>
    <td align="right">5.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.78</td>
    <td align="right">4.93</td>
    <td align="right">11.26</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">8.45</td>
    <td align="right">4.99</td>
    <td align="right">10.47</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">10.81</td>
    <td align="right">9.48</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.80</td>
    <td align="right">5.56</td>
    <td align="right">9.95</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">9.95</td>
    <td align="right">6.97</td>
    <td align="right">12.39</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.92</td>
    <td align="right">8.32</td>
    <td align="right">7.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">8.25</td>
    <td align="right">7.45</td>
    <td align="right">11.67</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">11.66</td>
    <td align="right">6.81</td>
    <td align="right">10.69</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.12</td>
    <td align="right">11.70</td>
    <td align="right">11.69</td>
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
    <td align="right">27.77</td>
    <td align="right">12.35</td>
    <td align="right">8.59</td>
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
    <td align="right">9.28</td>
    <td align="right">9.55</td>
    <td align="right">16.23</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.84</td>
    <td align="right">3.20</td>
    <td align="right">3.33</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.03</td>
    <td align="right">3.52</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.66</td>
    <td align="right">21.68</td>
    <td align="right">20.76</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.02</td>
    <td align="right">5.66</td>
    <td align="right">5.78</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.19</td>
    <td align="right">5.00</td>
    <td align="right">6.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.97</td>
    <td align="right">36.82</td>
    <td align="right">23.40</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.93</td>
    <td align="right">8.30</td>
    <td align="right">8.27</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.43</td>
    <td align="right">8.95</td>
    <td align="right">8.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">73.40</td>
    <td align="right">49.16</td>
    <td align="right">25.53</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">11.52</td>
    <td align="right">9.30</td>
    <td align="right">9.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.84</td>
    <td align="right">8.11</td>
    <td align="right">8.14</td>
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
    <td align="right">3.36</td>
    <td align="right">4.28</td>
    <td align="right">3.91</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.64</td>
    <td align="right">3.74</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.98</td>
    <td align="right">3.86</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.21</td>
    <td align="right">8.12</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.92</td>
    <td align="right">4.96</td>
    <td align="right">7.47</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.06</td>
    <td align="right">5.78</td>
    <td align="right">6.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">14.36</td>
    <td align="right">11.78</td>
    <td align="right">12.02</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.23</td>
    <td align="right">14.30</td>
    <td align="right">13.54</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.22</td>
    <td align="right">10.30</td>
    <td align="right">7.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">18.51</td>
    <td align="right">16.32</td>
    <td align="right">16.87</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.17</td>
    <td align="right">18.48</td>
    <td align="right">19.48</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">11.46</td>
    <td align="right">13.49</td>
    <td align="right">8.76</td>
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
    <td align="right">3.11</td>
    <td align="right">3.74</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.54</td>
    <td align="right">2.98</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.87</td>
    <td align="right">3.75</td>
    <td align="right">3.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.84</td>
    <td align="right">2.98</td>
    <td align="right">2.96</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.85</td>
    <td align="right">4.48</td>
    <td align="right">4.47</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.09</td>
    <td align="right">4.44</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">7.32</td>
    <td align="right">7.45</td>
    <td align="right">5.02</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">9.70</td>
    <td align="right">8.84</td>
    <td align="right">8.83</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">9.95</td>
    <td align="right">8.67</td>
    <td align="right">9.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.46</td>
    <td align="right">10.22</td>
    <td align="right">5.97</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.22</td>
    <td align="right">12.16</td>
    <td align="right">12.31</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.23</td>
    <td align="right">13.21</td>
    <td align="right">13.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">4.58</td>
    <td align="right">4.17</td>
    <td align="right">11.18</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">8.83</td>
    <td align="right">4.92</td>
    <td align="right">13.55</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">9.19</td>
    <td align="right">7.53</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">8.14</td>
    <td align="right">7.16</td>
    <td align="right">11.96</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">12.63</td>
    <td align="right">7.52</td>
    <td align="right">12.51</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">13.42</td>
    <td align="right">11.93</td>
    <td align="right">12.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">14.55</td>
    <td align="right">12.44</td>
    <td align="right">13.69</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">21.00</td>
    <td align="right">14.18</td>
    <td align="right">15.75</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">22.10</td>
    <td align="right">20.17</td>
    <td align="right">20.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">23.92</td>
    <td align="right">19.81</td>
    <td align="right">15.82</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.45</td>
    <td align="right">19.20</td>
    <td align="right">16.76</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">40.96</td>
    <td align="right">35.86</td>
    <td align="right">36.21</td>
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
    <td align="right">35.69</td>
    <td align="right">6.21</td>
    <td align="right">3.78</td>
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
    <td align="right">12.02</td>
    <td align="right">12.38</td>
    <td align="right">16.96</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.23</td>
    <td align="right">4.27</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.99</td>
    <td align="right">5.25</td>
    <td align="right">5.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.48</td>
    <td align="right">17.70</td>
    <td align="right">17.59</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.93</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.02</td>
    <td align="right">5.93</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.79</td>
    <td align="right">21.31</td>
    <td align="right">16.57</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.60</td>
    <td align="right">5.34</td>
    <td align="right">5.43</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.30</td>
    <td align="right">6.87</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.03</td>
    <td align="right">27.48</td>
    <td align="right">17.21</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.90</td>
    <td align="right">5.89</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.36</td>
    <td align="right">7.42</td>
    <td align="right">7.37</td>
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
    <td align="right">7.85</td>
    <td align="right">5.54</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.21</td>
    <td align="right">5.87</td>
    <td align="right">5.67</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.39</td>
    <td align="right">3.93</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.24</td>
    <td align="right">8.18</td>
    <td align="right">8.17</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.26</td>
    <td align="right">8.71</td>
    <td align="right">8.69</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.92</td>
    <td align="right">4.94</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.49</td>
    <td align="right">10.77</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.91</td>
    <td align="right">10.78</td>
    <td align="right">10.73</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.95</td>
    <td align="right">7.06</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.27</td>
    <td align="right">14.24</td>
    <td align="right">14.29</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.78</td>
    <td align="right">13.70</td>
    <td align="right">12.78</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.06</td>
    <td align="right">7.24</td>
    <td align="right">5.48</td>
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
    <td align="right">3.30</td>
    <td align="right">3.83</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.50</td>
    <td align="right">5.49</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.76</td>
    <td align="right">5.38</td>
    <td align="right">5.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.27</td>
    <td align="right">5.63</td>
    <td align="right">4.66</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.89</td>
    <td align="right">5.92</td>
    <td align="right">5.06</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">7.00</td>
    <td align="right">6.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.07</td>
    <td align="right">6.80</td>
    <td align="right">5.01</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.94</td>
    <td align="right">9.39</td>
    <td align="right">7.61</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.95</td>
    <td align="right">9.37</td>
    <td align="right">7.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.17</td>
    <td align="right">7.02</td>
    <td align="right">5.18</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.15</td>
    <td align="right">10.66</td>
    <td align="right">7.78</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.31</td>
    <td align="right">10.50</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.2994</td>
    <td align="right">8.93</td>
    <td align="right">8.59</td>
    <td align="right">13.69</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.06</td>
    <td align="right">11.69</td>
    <td align="right">17.13</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.83</td>
    <td align="right">11.83</td>
    <td align="right">12.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.99</td>
    <td align="right">11.69</td>
    <td align="right">14.46</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">14.61</td>
    <td align="right">13.61</td>
    <td align="right">16.00</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">18.76</td>
    <td align="right">19.02</td>
    <td align="right">17.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.28</td>
    <td align="right">14.57</td>
    <td align="right">14.38</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.42</td>
    <td align="right">17.45</td>
    <td align="right">15.49</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">22.60</td>
    <td align="right">19.92</td>
    <td align="right">18.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.30</td>
    <td align="right">17.31</td>
    <td align="right">15.31</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.49</td>
    <td align="right">20.40</td>
    <td align="right">14.98</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">30.19</td>
    <td align="right">28.27</td>
    <td align="right">28.45</td>
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
    <td align="right">45.38</td>
    <td align="right">21.79</td>
    <td align="right">8.84</td>
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
    <td align="right">14.72</td>
    <td align="right">13.04</td>
    <td align="right">17.66</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.18</td>
    <td align="right">4.62</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.17</td>
    <td align="right">5.57</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">28.93</td>
    <td align="right">20.79</td>
    <td align="right">19.05</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.71</td>
    <td align="right">5.12</td>
    <td align="right">5.21</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">10.35</td>
    <td align="right">7.69</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">36.83</td>
    <td align="right">38.39</td>
    <td align="right">20.78</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">18.05</td>
    <td align="right">12.23</td>
    <td align="right">12.67</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.06</td>
    <td align="right">20.86</td>
    <td align="right">11.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">79.70</td>
    <td align="right">81.01</td>
    <td align="right">24.51</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.43</td>
    <td align="right">17.03</td>
    <td align="right">19.48</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">24.64</td>
    <td align="right">20.02</td>
    <td align="right">22.26</td>
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
    <td align="right">6.30</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.52</td>
    <td align="right">6.43</td>
    <td align="right">6.57</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.79</td>
    <td align="right">4.20</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">16.87</td>
    <td align="right">10.64</td>
    <td align="right">10.89</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">21.68</td>
    <td align="right">12.27</td>
    <td align="right">12.38</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.40</td>
    <td align="right">5.63</td>
    <td align="right">5.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">27.97</td>
    <td align="right">24.62</td>
    <td align="right">21.80</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.18</td>
    <td align="right">15.91</td>
    <td align="right">17.84</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.12</td>
    <td align="right">17.37</td>
    <td align="right">14.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">34.20</td>
    <td align="right">32.52</td>
    <td align="right">32.13</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">36.16</td>
    <td align="right">27.18</td>
    <td align="right">25.18</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.72</td>
    <td align="right">22.45</td>
    <td align="right">13.61</td>
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
    <td align="right">3.71</td>
    <td align="right">4.11</td>
    <td align="right">4.15</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.07</td>
    <td align="right">6.04</td>
    <td align="right">6.01</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.17</td>
    <td align="right">5.75</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.99</td>
    <td align="right">7.42</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.47</td>
    <td align="right">6.78</td>
    <td align="right">5.86</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.14</td>
    <td align="right">8.14</td>
    <td align="right">7.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">10.17</td>
    <td align="right">12.24</td>
    <td align="right">9.14</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">14.08</td>
    <td align="right">13.47</td>
    <td align="right">11.41</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">13.11</td>
    <td align="right">12.24</td>
    <td align="right">9.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">13.43</td>
    <td align="right">16.02</td>
    <td align="right">14.39</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">21.17</td>
    <td align="right">23.27</td>
    <td align="right">18.75</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">24.10</td>
    <td align="right">20.85</td>
    <td align="right">16.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3301</td>
    <td align="right">10.46</td>
    <td align="right">9.69</td>
    <td align="right">14.19</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">13.41</td>
    <td align="right">12.65</td>
    <td align="right">17.87</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">15.50</td>
    <td align="right">14.77</td>
    <td align="right">15.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.86</td>
    <td align="right">18.00</td>
    <td align="right">16.00</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">23.29</td>
    <td align="right">24.30</td>
    <td align="right">20.23</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">23.09</td>
    <td align="right">23.73</td>
    <td align="right">24.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">35.80</td>
    <td align="right">30.75</td>
    <td align="right">22.27</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">43.18</td>
    <td align="right">47.41</td>
    <td align="right">17.68</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.97</td>
    <td align="right">26.21</td>
    <td align="right">28.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">43.18</td>
    <td align="right">42.30</td>
    <td align="right">25.39</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">54.22</td>
    <td align="right">51.35</td>
    <td align="right">22.82</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">47.72</td>
    <td align="right">43.55</td>
    <td align="right">44.30</td>
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
    <td align="right">64.11</td>
    <td align="right">41.21</td>
    <td align="right">18.35</td>
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
    <td align="right">27.45</td>
    <td align="right">42.17</td>
    <td align="right">36.60</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.56</td>
    <td align="right">15.61</td>
    <td align="right">15.71</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.11</td>
    <td align="right">19.27</td>
    <td align="right">19.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.35</td>
    <td align="right">63.55</td>
    <td align="right">39.61</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.32</td>
    <td align="right">19.62</td>
    <td align="right">19.66</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.15</td>
    <td align="right">18.68</td>
    <td align="right">18.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">45.48</td>
    <td align="right">78.73</td>
    <td align="right">38.32</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.41</td>
    <td align="right">18.59</td>
    <td align="right">18.51</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.18</td>
    <td align="right">18.30</td>
    <td align="right">18.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.32</td>
    <td align="right">96.85</td>
    <td align="right">37.85</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.17</td>
    <td align="right">18.76</td>
    <td align="right">18.80</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.00</td>
    <td align="right">19.94</td>
    <td align="right">19.90</td>
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
    <td align="right">16.15</td>
    <td align="right">21.26</td>
    <td align="right">21.21</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.54</td>
    <td align="right">22.32</td>
    <td align="right">22.32</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.96</td>
    <td align="right">13.58</td>
    <td align="right">13.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.32</td>
    <td align="right">26.03</td>
    <td align="right">26.00</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.59</td>
    <td align="right">27.69</td>
    <td align="right">27.67</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.89</td>
    <td align="right">15.87</td>
    <td align="right">15.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.18</td>
    <td align="right">33.10</td>
    <td align="right">33.04</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.97</td>
    <td align="right">46.65</td>
    <td align="right">46.56</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.99</td>
    <td align="right">19.56</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.13</td>
    <td align="right">35.93</td>
    <td align="right">35.80</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.66</td>
    <td align="right">56.53</td>
    <td align="right">56.40</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.50</td>
    <td align="right">25.56</td>
    <td align="right">25.53</td>
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
    <td align="right">15.49</td>
    <td align="right">15.59</td>
    <td align="right">15.57</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.15</td>
    <td align="right">21.28</td>
    <td align="right">21.25</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.82</td>
    <td align="right">22.26</td>
    <td align="right">22.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">20.02</td>
    <td align="right">20.55</td>
    <td align="right">20.57</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.31</td>
    <td align="right">26.00</td>
    <td align="right">26.01</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.56</td>
    <td align="right">27.64</td>
    <td align="right">27.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.36</td>
    <td align="right">24.90</td>
    <td align="right">24.91</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.19</td>
    <td align="right">33.06</td>
    <td align="right">33.05</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">63.77</td>
    <td align="right">46.63</td>
    <td align="right">46.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.25</td>
    <td align="right">37.07</td>
    <td align="right">37.03</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.25</td>
    <td align="right">35.91</td>
    <td align="right">35.88</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.77</td>
    <td align="right">56.49</td>
    <td align="right">56.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">17.11</td>
    <td align="right">20.75</td>
    <td align="right">25.41</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.18</td>
    <td align="right">29.20</td>
    <td align="right">34.47</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.35</td>
    <td align="right">30.01</td>
    <td align="right">30.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.41</td>
    <td align="right">28.06</td>
    <td align="right">25.88</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.44</td>
    <td align="right">34.01</td>
    <td align="right">32.64</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">38.30</td>
    <td align="right">38.94</td>
    <td align="right">38.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.49</td>
    <td align="right">33.58</td>
    <td align="right">25.97</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.99</td>
    <td align="right">41.73</td>
    <td align="right">34.02</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.83</td>
    <td align="right">41.67</td>
    <td align="right">41.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.48</td>
    <td align="right">40.26</td>
    <td align="right">27.05</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">50.81</td>
    <td align="right">43.82</td>
    <td align="right">31.62</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">55.01</td>
    <td align="right">59.24</td>
    <td align="right">59.12</td>
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
    <td align="right">75.11</td>
    <td align="right">111.96</td>
    <td align="right">21.31</td>
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
    <td align="right">28.50</td>
    <td align="right">46.93</td>
    <td align="right">40.43</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.06</td>
    <td align="right">16.06</td>
    <td align="right">16.21</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.86</td>
    <td align="right">19.76</td>
    <td align="right">19.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">38.28</td>
    <td align="right">65.18</td>
    <td align="right">42.59</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">18.54</td>
    <td align="right">21.00</td>
    <td align="right">20.55</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.82</td>
    <td align="right">19.96</td>
    <td align="right">24.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">59.35</td>
    <td align="right">102.43</td>
    <td align="right">50.33</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">21.26</td>
    <td align="right">28.35</td>
    <td align="right">26.47</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">25.01</td>
    <td align="right">29.81</td>
    <td align="right">29.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">127.22</td>
    <td align="right">195.38</td>
    <td align="right">75.05</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">58.16</td>
    <td align="right">49.75</td>
    <td align="right">52.91</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">58.42</td>
    <td align="right">54.30</td>
    <td align="right">44.72</td>
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
    <td align="right">18.35</td>
    <td align="right">23.74</td>
    <td align="right">23.81</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">38.13</td>
    <td align="right">24.10</td>
    <td align="right">24.33</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.44</td>
    <td align="right">14.19</td>
    <td align="right">14.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.90</td>
    <td align="right">33.69</td>
    <td align="right">29.92</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">59.86</td>
    <td align="right">37.95</td>
    <td align="right">37.61</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">14.22</td>
    <td align="right">17.30</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">52.80</td>
    <td align="right">56.52</td>
    <td align="right">58.14</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">78.44</td>
    <td align="right">96.86</td>
    <td align="right">75.22</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">38.19</td>
    <td align="right">38.63</td>
    <td align="right">39.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">72.24</td>
    <td align="right">88.15</td>
    <td align="right">82.18</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">123.61</td>
    <td align="right">98.87</td>
    <td align="right">98.73</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">61.08</td>
    <td align="right">76.87</td>
    <td align="right">95.63</td>
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
    <td align="right">39.32</td>
    <td align="right">20.03</td>
    <td align="right">17.20</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">43.25</td>
    <td align="right">27.14</td>
    <td align="right">44.42</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">64.04</td>
    <td align="right">27.10</td>
    <td align="right">24.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">27.11</td>
    <td align="right">28.17</td>
    <td align="right">29.16</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">27.22</td>
    <td align="right">31.87</td>
    <td align="right">30.55</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.60</td>
    <td align="right">85.20</td>
    <td align="right">40.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">52.20</td>
    <td align="right">40.05</td>
    <td align="right">42.12</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">42.82</td>
    <td align="right">48.81</td>
    <td align="right">45.96</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">84.31</td>
    <td align="right">69.50</td>
    <td align="right">70.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">54.13</td>
    <td align="right">58.09</td>
    <td align="right">62.51</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">46.87</td>
    <td align="right">66.94</td>
    <td align="right">50.54</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.97</td>
    <td align="right">62.73</td>
    <td align="right">61.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">17.88</td>
    <td align="right">21.88</td>
    <td align="right">26.73</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">33.01</td>
    <td align="right">30.57</td>
    <td align="right">39.50</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.37</td>
    <td align="right">32.74</td>
    <td align="right">32.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">28.50</td>
    <td align="right">29.47</td>
    <td align="right">26.52</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">42.52</td>
    <td align="right">36.94</td>
    <td align="right">33.84</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.20</td>
    <td align="right">40.47</td>
    <td align="right">40.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">44.29</td>
    <td align="right">40.98</td>
    <td align="right">29.58</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">76.10</td>
    <td align="right">97.77</td>
    <td align="right">61.13</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">49.88</td>
    <td align="right">54.66</td>
    <td align="right">54.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">93.16</td>
    <td align="right">84.21</td>
    <td align="right">50.02</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">88.89</td>
    <td align="right">83.68</td>
    <td align="right">50.71</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">81.93</td>
    <td align="right">75.66</td>
    <td align="right">70.47</td>
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
    <td align="right">62.26</td>
    <td align="right">10.27</td>
    <td align="right">6.91</td>
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
    <td align="right">13.79</td>
    <td align="right">22.62</td>
    <td align="right">26.74</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.60</td>
    <td align="right">12.49</td>
    <td align="right">12.97</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.80</td>
    <td align="right">13.91</td>
    <td align="right">13.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.34</td>
    <td align="right">35.19</td>
    <td align="right">28.93</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.23</td>
    <td align="right">14.19</td>
    <td align="right">14.20</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.55</td>
    <td align="right">15.42</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.84</td>
    <td align="right">47.29</td>
    <td align="right">30.40</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.89</td>
    <td align="right">15.51</td>
    <td align="right">15.55</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.67</td>
    <td align="right">16.79</td>
    <td align="right">16.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.16</td>
    <td align="right">60.22</td>
    <td align="right">30.96</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.60</td>
    <td align="right">16.37</td>
    <td align="right">16.39</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.95</td>
    <td align="right">17.95</td>
    <td align="right">17.93</td>
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
    <td align="right">12.74</td>
    <td align="right">16.13</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.27</td>
    <td align="right">16.75</td>
    <td align="right">16.72</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.12</td>
    <td align="right">9.38</td>
    <td align="right">9.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.47</td>
    <td align="right">22.53</td>
    <td align="right">22.52</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.32</td>
    <td align="right">22.30</td>
    <td align="right">22.32</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.43</td>
    <td align="right">13.99</td>
    <td align="right">14.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.05</td>
    <td align="right">32.29</td>
    <td align="right">32.34</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.58</td>
    <td align="right">30.68</td>
    <td align="right">30.71</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.46</td>
    <td align="right">17.51</td>
    <td align="right">17.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.89</td>
    <td align="right">36.08</td>
    <td align="right">36.07</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.92</td>
    <td align="right">35.87</td>
    <td align="right">35.78</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.36</td>
    <td align="right">20.40</td>
    <td align="right">20.38</td>
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
    <td align="right">6.57</td>
    <td align="right">9.40</td>
    <td align="right">9.40</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.87</td>
    <td align="right">16.08</td>
    <td align="right">16.08</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.29</td>
    <td align="right">16.73</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.94</td>
    <td align="right">13.69</td>
    <td align="right">13.70</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.38</td>
    <td align="right">22.51</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.31</td>
    <td align="right">22.32</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.48</td>
    <td align="right">17.60</td>
    <td align="right">17.59</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.98</td>
    <td align="right">32.33</td>
    <td align="right">32.29</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.56</td>
    <td align="right">30.69</td>
    <td align="right">30.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.08</td>
    <td align="right">20.96</td>
    <td align="right">20.86</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.96</td>
    <td align="right">36.06</td>
    <td align="right">36.05</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.92</td>
    <td align="right">35.85</td>
    <td align="right">35.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">13.09</td>
    <td align="right">16.43</td>
    <td align="right">20.00</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.81</td>
    <td align="right">33.10</td>
    <td align="right">37.07</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.61</td>
    <td align="right">24.22</td>
    <td align="right">23.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.96</td>
    <td align="right">23.66</td>
    <td align="right">20.71</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.76</td>
    <td align="right">38.62</td>
    <td align="right">36.48</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.00</td>
    <td align="right">31.86</td>
    <td align="right">31.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.11</td>
    <td align="right">30.41</td>
    <td align="right">20.37</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">60.39</td>
    <td align="right">45.72</td>
    <td align="right">37.06</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.14</td>
    <td align="right">35.45</td>
    <td align="right">35.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.19</td>
    <td align="right">38.77</td>
    <td align="right">25.08</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">65.62</td>
    <td align="right">51.64</td>
    <td align="right">40.07</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">41.76</td>
    <td align="right">45.98</td>
    <td align="right">45.77</td>
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
    <td align="right">75.34</td>
    <td align="right">43.93</td>
    <td align="right">10.53</td>
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
    <td align="right">14.28</td>
    <td align="right">23.30</td>
    <td align="right">28.76</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.81</td>
    <td align="right">12.80</td>
    <td align="right">12.78</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.10</td>
    <td align="right">14.22</td>
    <td align="right">14.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.25</td>
    <td align="right">34.28</td>
    <td align="right">29.49</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.93</td>
    <td align="right">13.92</td>
    <td align="right">13.91</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.39</td>
    <td align="right">15.08</td>
    <td align="right">15.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.44</td>
    <td align="right">47.28</td>
    <td align="right">30.56</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.73</td>
    <td align="right">15.08</td>
    <td align="right">15.11</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.58</td>
    <td align="right">16.45</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">30.65</td>
    <td align="right">61.01</td>
    <td align="right">30.97</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.76</td>
    <td align="right">16.19</td>
    <td align="right">16.23</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.78</td>
    <td align="right">17.72</td>
    <td align="right">17.88</td>
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
    <td align="right">13.25</td>
    <td align="right">17.02</td>
    <td align="right">17.03</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.59</td>
    <td align="right">18.02</td>
    <td align="right">18.03</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.38</td>
    <td align="right">9.69</td>
    <td align="right">9.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.02</td>
    <td align="right">22.09</td>
    <td align="right">22.07</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.41</td>
    <td align="right">22.04</td>
    <td align="right">22.07</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.25</td>
    <td align="right">14.09</td>
    <td align="right">14.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">26.57</td>
    <td align="right">35.13</td>
    <td align="right">33.84</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">29.07</td>
    <td align="right">31.38</td>
    <td align="right">33.60</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">25.29</td>
    <td align="right">33.35</td>
    <td align="right">21.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">47.72</td>
    <td align="right">61.31</td>
    <td align="right">77.58</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">76.03</td>
    <td align="right">76.63</td>
    <td align="right">72.14</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">39.24</td>
    <td align="right">60.46</td>
    <td align="right">54.98</td>
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
    <td align="right">7.42</td>
    <td align="right">10.49</td>
    <td align="right">9.92</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.25</td>
    <td align="right">17.08</td>
    <td align="right">17.36</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.62</td>
    <td align="right">18.17</td>
    <td align="right">18.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">12.38</td>
    <td align="right">15.21</td>
    <td align="right">15.64</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">19.19</td>
    <td align="right">26.57</td>
    <td align="right">22.48</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">19.40</td>
    <td align="right">24.35</td>
    <td align="right">23.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">19.46</td>
    <td align="right">19.39</td>
    <td align="right">19.28</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.83</td>
    <td align="right">34.91</td>
    <td align="right">35.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.66</td>
    <td align="right">32.16</td>
    <td align="right">32.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">20.47</td>
    <td align="right">25.37</td>
    <td align="right">25.69</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">31.67</td>
    <td align="right">41.55</td>
    <td align="right">42.35</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">37.25</td>
    <td align="right">39.24</td>
    <td align="right">39.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">13.69</td>
    <td align="right">16.90</td>
    <td align="right">20.60</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">49.30</td>
    <td align="right">34.39</td>
    <td align="right">37.97</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">22.28</td>
    <td align="right">26.34</td>
    <td align="right">26.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">21.58</td>
    <td align="right">25.02</td>
    <td align="right">22.36</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">60.04</td>
    <td align="right">38.44</td>
    <td align="right">36.42</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">30.83</td>
    <td align="right">33.85</td>
    <td align="right">33.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">26.01</td>
    <td align="right">33.12</td>
    <td align="right">21.55</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">63.36</td>
    <td align="right">48.89</td>
    <td align="right">40.09</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">34.31</td>
    <td align="right">38.08</td>
    <td align="right">38.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">56.02</td>
    <td align="right">60.66</td>
    <td align="right">34.04</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">97.73</td>
    <td align="right">83.69</td>
    <td align="right">57.54</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">50.67</td>
    <td align="right">55.23</td>
    <td align="right">54.90</td>
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
    <td align="right">42.22</td>
    <td align="right">8.57</td>
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
    <td align="right">2.1546</td>
    <td align="right">59.10</td>
    <td align="right">54.97</td>
    <td align="right">41.78</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.80</td>
    <td align="right">20.53</td>
    <td align="right">24.48</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.15</td>
    <td align="right">26.12</td>
    <td align="right">29.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">90.00</td>
    <td align="right">80.57</td>
    <td align="right">44.03</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.98</td>
    <td align="right">22.06</td>
    <td align="right">24.15</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.39</td>
    <td align="right">28.35</td>
    <td align="right">30.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.52</td>
    <td align="right">97.96</td>
    <td align="right">43.28</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.50</td>
    <td align="right">22.82</td>
    <td align="right">24.34</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.76</td>
    <td align="right">30.97</td>
    <td align="right">32.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">140.28</td>
    <td align="right">123.06</td>
    <td align="right">45.16</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.41</td>
    <td align="right">24.19</td>
    <td align="right">25.16</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">31.46</td>
    <td align="right">33.90</td>
    <td align="right">34.32</td>
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
    <td align="right">23.43</td>
    <td align="right">43.15</td>
    <td align="right">43.68</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.62</td>
    <td align="right">43.17</td>
    <td align="right">43.32</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.64</td>
    <td align="right">24.96</td>
    <td align="right">24.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.23</td>
    <td align="right">58.40</td>
    <td align="right">58.87</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.80</td>
    <td align="right">59.64</td>
    <td align="right">59.15</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.75</td>
    <td align="right">36.54</td>
    <td align="right">25.92</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.10</td>
    <td align="right">80.01</td>
    <td align="right">80.54</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">45.19</td>
    <td align="right">80.59</td>
    <td align="right">80.64</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">29.05</td>
    <td align="right">55.23</td>
    <td align="right">40.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">49.10</td>
    <td align="right">88.59</td>
    <td align="right">88.79</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.77</td>
    <td align="right">95.62</td>
    <td align="right">95.61</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.34</td>
    <td align="right">55.91</td>
    <td align="right">40.62</td>
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
    <td align="right">26.28</td>
    <td align="right">26.19</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.66</td>
    <td align="right">29.27</td>
    <td align="right">29.23</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.87</td>
    <td align="right">30.97</td>
    <td align="right">30.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.08</td>
    <td align="right">46.94</td>
    <td align="right">35.11</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.48</td>
    <td align="right">39.91</td>
    <td align="right">27.82</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.09</td>
    <td align="right">52.15</td>
    <td align="right">40.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.86</td>
    <td align="right">54.81</td>
    <td align="right">39.52</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.20</td>
    <td align="right">53.42</td>
    <td align="right">35.48</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.26</td>
    <td align="right">61.43</td>
    <td align="right">44.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.96</td>
    <td align="right">55.58</td>
    <td align="right">39.71</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.87</td>
    <td align="right">64.56</td>
    <td align="right">44.47</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.64</td>
    <td align="right">64.10</td>
    <td align="right">44.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3219</td>
    <td align="right">25.63</td>
    <td align="right">43.73</td>
    <td align="right">36.01</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.17</td>
    <td align="right">55.86</td>
    <td align="right">42.01</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">36.99</td>
    <td align="right">62.50</td>
    <td align="right">62.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">36.44</td>
    <td align="right">61.22</td>
    <td align="right">36.89</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.88</td>
    <td align="right">64.36</td>
    <td align="right">39.94</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.14</td>
    <td align="right">81.00</td>
    <td align="right">81.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">41.22</td>
    <td align="right">73.99</td>
    <td align="right">37.13</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.67</td>
    <td align="right">81.00</td>
    <td align="right">42.28</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.46</td>
    <td align="right">87.72</td>
    <td align="right">87.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.97</td>
    <td align="right">94.49</td>
    <td align="right">38.56</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.88</td>
    <td align="right">97.89</td>
    <td align="right">41.33</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.20</td>
    <td align="right">126.23</td>
    <td align="right">125.12</td>
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
    <td align="right">62.50</td>
    <td align="right">36.86</td>
    <td align="right">11.04</td>
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
    <td align="right">60.04</td>
    <td align="right">46.57</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.34</td>
    <td align="right">21.80</td>
    <td align="right">26.68</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.02</td>
    <td align="right">29.26</td>
    <td align="right">33.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">98.11</td>
    <td align="right">85.69</td>
    <td align="right">47.53</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.12</td>
    <td align="right">31.15</td>
    <td align="right">33.69</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">30.90</td>
    <td align="right">30.91</td>
    <td align="right">34.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">121.83</td>
    <td align="right">106.45</td>
    <td align="right">46.65</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">28.38</td>
    <td align="right">25.18</td>
    <td align="right">26.73</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">33.58</td>
    <td align="right">42.20</td>
    <td align="right">45.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">223.42</td>
    <td align="right">227.27</td>
    <td align="right">54.81</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">44.65</td>
    <td align="right">33.00</td>
    <td align="right">33.33</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">45.27</td>
    <td align="right">52.61</td>
    <td align="right">63.32</td>
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
    <td align="right">26.03</td>
    <td align="right">44.17</td>
    <td align="right">44.30</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.22</td>
    <td align="right">44.48</td>
    <td align="right">44.49</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">20.35</td>
    <td align="right">30.03</td>
    <td align="right">29.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.07</td>
    <td align="right">69.38</td>
    <td align="right">71.90</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">45.64</td>
    <td align="right">67.60</td>
    <td align="right">67.98</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">20.05</td>
    <td align="right">41.94</td>
    <td align="right">31.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">50.36</td>
    <td align="right">86.31</td>
    <td align="right">88.32</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">55.94</td>
    <td align="right">92.28</td>
    <td align="right">96.18</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">46.88</td>
    <td align="right">99.26</td>
    <td align="right">78.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">63.66</td>
    <td align="right">102.37</td>
    <td align="right">109.34</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">85.72</td>
    <td align="right">132.43</td>
    <td align="right">130.15</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">59.90</td>
    <td align="right">104.85</td>
    <td align="right">122.42</td>
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
    <td align="right">20.40</td>
    <td align="right">47.90</td>
    <td align="right">41.44</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">22.42</td>
    <td align="right">34.95</td>
    <td align="right">42.96</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">24.69</td>
    <td align="right">37.72</td>
    <td align="right">35.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.50</td>
    <td align="right">52.09</td>
    <td align="right">40.45</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">23.59</td>
    <td align="right">47.47</td>
    <td align="right">32.12</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">26.05</td>
    <td align="right">61.30</td>
    <td align="right">63.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">51.51</td>
    <td align="right">98.02</td>
    <td align="right">99.87</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">84.10</td>
    <td align="right">103.42</td>
    <td align="right">43.23</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">37.70</td>
    <td align="right">103.08</td>
    <td align="right">75.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">68.41</td>
    <td align="right">117.74</td>
    <td align="right">60.91</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">47.85</td>
    <td align="right">92.26</td>
    <td align="right">68.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">42.13</td>
    <td align="right">89.84</td>
    <td align="right">73.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
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
    <td align="right">2.3203</td>
    <td align="right">28.68</td>
    <td align="right">45.05</td>
    <td align="right">39.96</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">42.47</td>
    <td align="right">68.10</td>
    <td align="right">54.68</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">42.15</td>
    <td align="right">63.91</td>
    <td align="right">65.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">49.67</td>
    <td align="right">76.60</td>
    <td align="right">50.50</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">67.68</td>
    <td align="right">80.61</td>
    <td align="right">51.78</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">50.30</td>
    <td align="right">83.09</td>
    <td align="right">83.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">66.79</td>
    <td align="right">81.41</td>
    <td align="right">41.63</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">81.86</td>
    <td align="right">103.33</td>
    <td align="right">74.08</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">55.89</td>
    <td align="right">123.84</td>
    <td align="right">118.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">73.98</td>
    <td align="right">147.33</td>
    <td align="right">68.97</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">134.42</td>
    <td align="right">162.36</td>
    <td align="right">87.40</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">110.03</td>
    <td align="right">147.37</td>
    <td align="right">157.19</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
